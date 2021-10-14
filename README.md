# ph-asm

## Compiling

- Download the following programs and place their .exe files in the `utilities/` folder
  - `armips.exe` from [ARMIPS assembler](https://github.com/Kingcom/armips)
  - `blz.exe` from [CUE's NDS/GBA Compressors](https://www.romhacking.net/utilities/826/)
  - `fixy9.exe` and `makearm9.exe` from the [D-Pad patch](https://github.com/StraDaMa/Legend-of-Zelda-Phantom-Hourglass-D-Pad-Patch) repo
  - `ndstool.exe` - there's multiple places you can get this from, one of them is [DSLazy](https://www.romhacking.net/utilities/793/)
- Place a valid TLoZ: Phantom Hourglass ROM in the root of the cloned repo and name it `in.nds`
- Run `unpack.py` with your installed Python runtime
- Run `build.py` with your installed Python runtime
