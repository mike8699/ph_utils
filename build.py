#!/usr/bin/env python

from pathlib import Path
import shutil, subprocess, sys

def build_arm9(argv: list[str]):
    subprocess.run([Path('utils/armips.exe'), 'main.asm'])
    subprocess.run([Path('utils/blz.exe'), '-eo', 'arm9_compressed.bin'])
    # TODO: do this manually instead of relying on makearm9.exe
    subprocess.run([Path('utils/makearm9.exe'), '-c', 'arm9_compressed.bin', 'arm9_header.bin', 'arm9.bin'])
    Path.unlink(Path('arm9_compressed.bin'))
    Path.unlink(Path('arm9_header.bin'))
    Path.unlink(Path('arm9_original.bin'))

    overlays = ('0000', '0031')

    for overlay in overlays:
        subprocess.run([Path('utils/blz.exe'), '-eo', f'overlay/overlay_{overlay}.bin'])
        shutil.copy(f'overlay/overlay_{overlay}.bin', f'overlay_{overlay}.bin')
    
    subprocess.run([Path('utils/fixy9.exe'), 'y9.bin'] + [f'overlay_{overlay}.bin' for overlay in overlays])

    for overlay in overlays:
        Path.unlink(Path(f'overlay_{overlay}.bin'))


def main(argv: list[str]):
    build_arm9([])
    subprocess.run([Path('utils/ndstool.exe'), '-c', 'out.nds', '-9', 'arm9.bin', '-7', 'arm7.bin', '-y9', 'y9.bin', '-y7', 'y7.bin', '-d', 'data', '-y', 'overlay', '-t', 'banner.bin', '-h', 'header.bin'])


if __name__ == '__main__':
    main(sys.argv)
