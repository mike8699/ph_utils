import os

from desmume.emulator import DeSmuME, DeSmuME_SDL_Window, SCREEN_HEIGHT, SCREEN_WIDTH

import pytest

class DesmumeEmulator:
    def __init__(self, rom_path: str, enable_sdl=False):
        self.emu: DeSmuME = DeSmuME()
        self.window: DeSmuME_SDL_Window
        if enable_sdl:
            self.window = self.emu.create_sdl_window()
        else:
            self.window = None
        self.frame = -1
        self.last_frame = -1
        self.emu.open(rom_path)

    def _next_frame(self):
        self.emu.cycle()
        if self.window is not None:
            self.window.process_input()
            self.window.draw()

    def wait(self, frames: int):
        """Idle the emulator for `frames` frames."""
        starting_frame = self.frame
        for _ in range(starting_frame, starting_frame + frames):
            self._next_frame()

    def touch_input(self, position: tuple[int, int], idle_frames: int = 0):
        """
        Touch screen at a given location.

        Params:
            position: tuple in the form of (x, y) representing the location to touch the screen.
            idle_frames: Optional number of frames to wait before touching the screen.
                         Shortcut for calling DesmumeEmulator.wait() before this method.
        """
        self.wait(idle_frames)
        x, y = position
        self.emu.input.touch_release()
        self._next_frame()
        self.emu.input.touch_set_pos(x, y)
        self._next_frame()
        self.emu.input.touch_release()


@pytest.fixture
def desmume_emulator() -> DesmumeEmulator:
    return DesmumeEmulator(rom_path=os.environ["PH_ROM_PATH"], enable_sdl=False)  # TODO: make enable_sdl configurable


@pytest.fixture
def emulator_at_file_select(desmume_emulator: DesmumeEmulator) -> DesmumeEmulator:
    desmume_emulator.touch_input((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 350)
    desmume_emulator.touch_input((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 400)
    return desmume_emulator
