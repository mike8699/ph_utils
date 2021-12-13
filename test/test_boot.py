import pytest

from test.conftest import DesmumeEmulator

def test_boot_new_game(emulator_at_file_select: DesmumeEmulator):
    """Test bootup from title screen, name entry, and intro CG."""
    emulator_at_file_select.touch_input(0, (130, 70))
