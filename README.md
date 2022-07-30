# DEPRECATION NOTICE

All of the code in this repo has been moved to and/or rewritten in this repo https://github.com/phst-randomizer/ph-randomizer.

# ph-utils

This is a collection of random code that modifies the base Legend of Zelda: Phantom Hourglass US ROM in various ways.
The goal is to eventually get to a point where we can put the game into a "completed"/"open" state as is required
for a randomizer. For now, this is mostly a collection of experimental assembly hacks and python code.

## Requirements
- Python 3.9 or higher (it may work on lower versions of Python 3, but proceed at your own risk)
- Windows or Linux
  - It's been tested on Windows 8/10; may or may not work on earlier or newer Windows versions.
  - For now, wine is required if running on Linux.

## Building the ROM

- Create a virtualenv and run `pip install -e .`
- Place a valid TLoZ: Phantom Hourglass ROM in the root of the cloned repo and name it `in.nds`
- Run `unpack.py` with your installed Python runtime
  - At this point you can make changes to `main.asm` if desired
- Run `build.py` with your installed Python runtime

## TODO

- Reimplement fixy9.exe in Python or something so this can be run on on-Windows machines without Wine
