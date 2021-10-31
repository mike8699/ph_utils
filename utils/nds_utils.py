import struct


def combine_arm9(
    arm9_data="arm9_compressed.bin",
    arm9_header="arm9_header.bin",
    arm9_output="arm9.bin",
):
    """Combines header and data into arm9.bin. Functionally the same as makearm9.bin -c"""
    with open(arm9_data, "rb") as input_arm9, open(
        arm9_header, "rb"
    ) as input_header, open(arm9_output, "wb") as output_arm9:
        data = input_header.read() + input_arm9.read()
        data = data[:0xB78] + struct.pack("<I", len(data) + 0x2000000) + data[0xB7C:]
        output_arm9.write(data)


def split_arm9(
    arm9_bin="arm9.bin", arm9_header="arm9_header.bin", arm9_output="arm9_original.bin"
):
    """Extract arm9 data + header into seperate files. Functionally the same as makearm9.bin -x"""
    with open(arm9_bin, "rb") as input_arm9, open(
        arm9_header, "wb"
    ) as output_header, open(arm9_output, "wb") as output_arm9:
        output_header.write(input_arm9.read(0x4000))
        data = input_arm9.read()
        data = data[: len(data) - 0xC]
        output_arm9.write(data)
