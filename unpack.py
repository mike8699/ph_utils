#!/usr/bin/env python

from pathlib import Path
import subprocess

def extract_arm9(argv: list[str]):
    subprocess.run([Path('utils/makearm9.exe'), '-x', 'arm9.bin', 'arm9_original.bin', 'arm9_header.bin'])
    subprocess.run([Path('utils/blz.exe'), '-d', 'arm9_original.bin'])

    overlays = ('0000', '0031')
    for overlay in overlays:
        subprocess.run([Path('utils/blz.exe'), '-d', f'overlay/overlay_{overlay}.bin'])

def main(argv: list[str]):
    subprocess.run([Path('utils/ndstool.exe'), '-v', '-x', 'in_dpad.nds', '-9', 'arm9.bin', '-7', 'arm7.bin', '-y9', 'y9.bin', '-y7', 'y7.bin', '-d', 'data', '-y', 'overlay', '-t', 'banner.bin', '-h', 'header.bin'])
    extract_arm9(argv)



if __name__ == '__main__':
    main([])
