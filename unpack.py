#!/usr/bin/env python

from pathlib import Path
import subprocess

def extract_arm9(argv: list[str]):
    
    # extract arm9 data + header into seperate files
    with open('arm9.bin', 'rb') as input_arm9, open(
        'arm9_header.bin', 'wb'
    ) as output_header, open('arm9_original.bin', 'wb') as output_arm9:
        output_header.write(input_arm9.read(0x4000))
        data = input_arm9.read()
        data = data[:len(data) - 0xC]
        output_arm9.write(data)

    subprocess.run([Path('utils/blz.exe'), '-d', 'arm9_original.bin'])

    overlays = ('0000', '0022', '0031')
    for overlay in overlays:
        subprocess.run([Path('utils/blz.exe'), '-d', f'overlay/overlay_{overlay}.bin'])

def main(argv: list[str]):
    subprocess.run([Path('utils/ndstool.exe'), '-v', '-x', 'in_dpad.nds', '-9', 'arm9.bin', '-7', 'arm7.bin', '-y9', 'y9.bin', '-y7', 'y7.bin', '-d', 'data', '-y', 'overlay', '-t', 'banner.bin', '-h', 'header.bin'])
    extract_arm9(argv)



if __name__ == '__main__':
    main([])
