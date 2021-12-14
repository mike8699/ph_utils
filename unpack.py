#!/usr/bin/env python

import os
from pathlib import Path
import subprocess

from utils.nds_utils import split_arm9


def blz_decomp(filename: str):
    try:
        subprocess.run([Path("utils/blz.exe"), "-d", filename])
    except FileNotFoundError:
        subprocess.run([Path("utils/blz"), "-d", filename])


def extract_arm9(argv: list[str]):

    split_arm9()

    blz_decomp("arm9_original.bin")

    overlays = ("0000", "0022", "0031")
    for overlay in overlays:
        blz_decomp(f"overlay/overlay_{overlay}.bin")


def main(argv: list[str]):
    subprocess.run(
        [
            Path(f"utils/ndstool{'.exe' if os.name == 'nt' else ''}"),
            "-v",
            "-x",
            "in_dpad.nds",
            "-9",
            "arm9.bin",
            "-7",
            "arm7.bin",
            "-y9",
            "y9.bin",
            "-y7",
            "y7.bin",
            "-d",
            "data",
            "-y",
            "overlay",
            "-t",
            "banner.bin",
            "-h",
            "header.bin",
        ]
    )
    extract_arm9(argv)


if __name__ == "__main__":
    main([])
