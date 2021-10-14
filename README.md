# ph-asm

## Requirements
- Python 3.9 or higher (it may work on lower versions of Python 3, but proceed at your own risk)
- Windows (tested on 8 and 10, not sure about other Windows versions)
  - This will eventually work on Linux, once I replace some of the Windows-only stuff with more universal tooling

## Compiling

- Place a valid TLoZ: Phantom Hourglass ROM in the root of the cloned repo and name it `in.nds`
- Run `unpack.py` with your installed Python runtime
  - At this point you can make changes to `main.asm` if desired
- Run `build.py` with your installed Python runtime

## TODO

- Reimplement fixy9.exe and makearm9.exe in Python or something so this can be run on non-Windows machines
