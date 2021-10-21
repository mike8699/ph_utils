#!/usr/bin/env python

from pathlib import Path
import shutil, subprocess, sys

from ndspy import narc, lz10
from zdspy.zdspy import zmb
from zdspy.ids import ITEM_IDS, OBJECT_IDS

def build_arm9():
    subprocess.run([Path('utils/armips.exe'), 'main.asm'])
    subprocess.run([Path('utils/blz.exe'), '-eo', 'arm9_compressed.bin'])
    # TODO: do this manually instead of relying on makearm9.exe
    subprocess.run([Path('utils/makearm9.exe'), '-c', 'arm9_compressed.bin', 'arm9_header.bin', 'arm9.bin'])
    Path.unlink(Path('arm9_compressed.bin'))
    Path.unlink(Path('arm9_header.bin'))
    Path.unlink(Path('arm9_original.bin'))

    overlays = ('0000', '0022', '0031')

    for overlay in overlays:
        subprocess.run([Path('utils/blz.exe'), '-eo', f'overlay/overlay_{overlay}.bin'])
        shutil.copy(f'overlay/overlay_{overlay}.bin', f'overlay_{overlay}.bin')
    
    subprocess.run([Path('utils/fixy9.exe'), 'y9.bin'] + [f'overlay_{overlay}.bin' for overlay in overlays])

    for overlay in overlays:
        Path.unlink(Path(f'overlay_{overlay}.bin'))


def fix_first_ocean_temple_chest(rom_root_dir: Path = Path.cwd()):
    """
    Puts a key in the first big chest in the Ocean Temple

    The first big chest in the Temple of the Ocean King is empty since
    Linebeck has already opened it. In the original game, Linebeck gives
    you the key when you save him. For the randomizer, the chest should
    contain the key.
    """
    filename = rom_root_dir / Path('data/Map/dngn_main/map00.bin')
    with open(filename, 'rb') as fd:
        narc_file = narc.NARC(lz10.decompress(fd.read()))
        zmb_file = zmb.ZMB(narc_file.getFileByName('zmb/dngn_main_00.zmb'))
        mpob: zmb.ZMB_MPOB = zmb_file.get_child('MPOB')
        mpob.children[34].item_id = 0x1 # put key in first TotOK chest
        narc_file.setFileByName('zmb/dngn_main_00.zmb', zmb_file.save())
        lz10.compressToFile((narc_file.save()), filename)


def build_data():
    fix_first_ocean_temple_chest()
    

def main(argv: list[str]):
    build_arm9()
    build_data()
    subprocess.run([Path('utils/ndstool.exe'), '-c', 'out.nds', '-9', 'arm9.bin', '-7', 'arm7.bin', '-y9', 'y9.bin', '-y7', 'y7.bin', '-d', 'data', '-y', 'overlay', '-t', 'banner.bin', '-h', 'header.bin'])


if __name__ == '__main__':
    main(sys.argv)
