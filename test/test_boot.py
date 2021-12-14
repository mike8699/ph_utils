from test.conftest import DesmumeEmulator


def test_boot_new_game(emulator_at_file_select: DesmumeEmulator):
    """Test bootup from title screen, name entry, and intro CG."""
    # Touch file
    emulator_at_file_select.touch_input((130, 70), 0)
    emulator_at_file_select.wait(100)

    # Confirm name
    emulator_at_file_select.touch_input((190, 180), 0)
    emulator_at_file_select.wait(100)

    # Click yes
    emulator_at_file_select.touch_input((210, 110), 0)
    emulator_at_file_select.wait(100)

    # Click right hand
    emulator_at_file_select.touch_input((210, 110), 0)
    emulator_at_file_select.wait(100)

    # Click yes
    emulator_at_file_select.touch_input((210, 110), 0)
    emulator_at_file_select.wait(100)

    # Click newly created file
    emulator_at_file_select.touch_input((130, 70), 0)
    emulator_at_file_select.wait(100)

    # Click it again
    emulator_at_file_select.touch_input((130, 70), 0)
    emulator_at_file_select.wait(100)

    # Click "Adventure"
    emulator_at_file_select.touch_input((130, 70), 0)
    emulator_at_file_select.wait(100)

    # TODO: make assertions about memory state of new game
