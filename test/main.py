import sys

from desmume.controls import Keys
from desmume.emulator import DeSmuME, DeSmuME_SDL_Window, SCREEN_HEIGHT, SCREEN_WIDTH

emu: DeSmuME = DeSmuME()
emu_memory = emu.memory
window: DeSmuME_SDL_Window = None

# from load_file import from_boot_start_first_file

def from_boot_start_first_file():
    for frame in range(500):
        if frame % 10 == 0:
            print(frame)
        emu.cycle()
        if window is not None:
            window.draw()


def main(rom_path: str):
    emu.open(rom_path)
    emu.input.keypad_rm_key(Keys.NB_KEYS)
    emu.input.keypad_rm_key(Keys.KEY_NONE)
    emu.input.keypad_rm_key(Keys.KEY_A)
    emu.input.keypad_rm_key(Keys.KEY_B)
    emu.input.keypad_rm_key(Keys.KEY_SELECT)
    emu.input.keypad_rm_key(Keys.KEY_START)
    emu.input.keypad_rm_key(Keys.KEY_RIGHT)
    emu.input.keypad_rm_key(Keys.KEY_LEFT)
    emu.input.keypad_rm_key(Keys.KEY_UP)
    emu.input.keypad_rm_key(Keys.KEY_DOWN)
    emu.input.keypad_rm_key(Keys.KEY_R)
    emu.input.keypad_rm_key(Keys.KEY_L)
    emu.input.keypad_rm_key(Keys.KEY_X)
    emu.input.keypad_rm_key(Keys.KEY_Y)
    emu.input.keypad_rm_key(Keys.KEY_DEBUG)
    emu.input.keypad_rm_key(Keys.KEY_BOOST)
    emu.input.keypad_rm_key(Keys.KEY_LID)
    emu.input.keypad_rm_key(Keys.NO_KEY_SET)

    # uncomment this to actually render the game window
    # window: DeSmuME_SDL_Window = emu.create_sdl_window()

    from_boot_start_first_file()

if __name__ == "__main__":
    main(sys.argv[1])
