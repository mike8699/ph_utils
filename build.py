#!/usr/bin/env python

from pathlib import Path
import os, shutil, struct, subprocess, sys

from ndspy import narc, lz10
from zdspy.randomizer.common import BMG_Location, ZMB_MPOB_Location
from zdspy.ids import ITEM_IDS, OBJECT_IDS

import randomizer
from utils.nds_utils import combine_arm9

def blz_comp(filename: str):
    try:
        subprocess.run([Path('utils/blz.exe'), '-eo', filename])
    except:
        subprocess.run([Path('utils/blz'), '-eo', filename])


def build_arm9():
    subprocess.run([Path('utils/armips.exe'), 'main.asm'])

    blz_comp('arm9_compressed.bin')

    # Recreate arm9.bin
    combine_arm9()

    Path('arm9_compressed.bin').unlink()
    Path('arm9_header.bin').unlink()
    Path('arm9_original.bin').unlink()

    overlays = ('0000', '0022', '0031')

    for overlay in overlays:
        blz_comp(f'overlay/overlay_{overlay}.bin')
        shutil.copy(f'overlay/overlay_{overlay}.bin', f'overlay_{overlay}.bin')
    
    run_y9 = [Path('utils/fixy9.exe'), 'y9.bin'] + [f'overlay_{overlay}.bin' for overlay in overlays]
    if os.name != 'nt':
        run_y9 = ['wine'] + run_y9

    subprocess.run(run_y9)

    for overlay in overlays:
        Path(f'overlay_{overlay}.bin').unlink()


def fix_first_ocean_temple_chest(rom_root_dir: Path = Path.cwd()):
    """
    Puts a key in the first big chest in the Ocean Temple

    The first big chest in the Temple of the Ocean King is empty since
    Linebeck has already opened it. In the original game, Linebeck gives
    you the key when you save him. For the randomizer, the chest should
    contain the key.
    """
    randomizer.set_location('ocean_temple_first_chest', 0x3)

def change_first_npcs_item(rom_root_dir: Path = Path.cwd()):
    """
    Changes first NPC (guy who has you clean his yard of rocks)
    reward from green rupee to yellow potion

    TODO: remove this once this is properly documented.
    """
    randomizer.set_location('mercay_island_rollable_tree', 0x77)

def build_data():
    # fix_first_ocean_temple_chest()
    change_first_npcs_item()
    # BMG_Location.save_all()
    # ZMB_MPOB_Location.save_all()


def main(argv: list[str]):
    # build_data()
    build_arm9()
    subprocess.run([Path(f"utils/ndstool{'.exe' if os.name == 'nt' else ''}"), '-c', 'out.nds', '-9', 'arm9.bin', '-7', 'arm7.bin', '-y9', 'y9.bin', '-y7', 'y7.bin', '-d', 'data', '-y', 'overlay', '-t', 'banner.bin', '-h', 'header.bin'])


if __name__ == '__main__':
    main(sys.argv)
