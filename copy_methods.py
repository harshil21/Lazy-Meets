import pyautogui as gui

import time

from get_clipboard import get_clipboard_content
from meeting_controls import close_participants_tab, open_participants_tab

selected_method = None


def copy_method_1(x: int, y: int) -> bool:
    """Try to copy by dragging over the string, and then use hotkey."""
    gui.moveTo(x + 15, y, 0)
    gui.mouseDown()
    gui.move(70, 0)
    gui.hotkey("ctrl", "c")
    gui.mouseUp()
    return check_copied()


def copy_method_2(x: int, y: int) -> bool:
    """Try to copy by dragging over the string, then right click to copy"""
    gui.moveTo(x + 15, y, 0)
    gui.mouseDown()
    gui.move(70, 0)
    gui.mouseUp()
    gui.click(button="right")
    gui.move(10, 10)
    gui.click()
    return check_copied()


def copy_method_3(_: int = None, y: int = None) -> bool:
    """Triple click, move cursor above, and copy using right click."""
    time.sleep(1)
    gui.tripleClick()
    time.sleep(1)
    gui.tripleClick()
    time.sleep(1.5)
    gui.move(0, -35)
    gui.click(button="right")
    gui.move(15, 15, 0)
    gui.click()
    return check_copied()


def copy_trier(x: int, y: int, tab_close: tuple) -> None:
    """Tries to copy the participant number (Microsoft can be troublesome)"""
    global selected_method

    if selected_method is not None:  # If a method worked previously, use it.
        gui.moveTo(x, y)
        selected_method(x, y)
        return
    i_x, i_y = tab_close

    for copy_method in (
        copy_method_1,
        copy_method_2,
        copy_method_3,
    ):
        gui.moveTo(x, y)  # Reset cursor
        if copy_method(x, y):  # If copy method worked, exit
            selected_method = copy_method
            break
        print(f"{copy_method.__name__} failed.")
        close_participants_tab(i_x, i_y)
        time.sleep(2)
        open_participants_tab(i_x, i_y)


def check_copied() -> bool:
    """Returns True if a number was copied."""
    try:
        copied = get_clipboard_content()
    except Exception as e:
        print(e)
        return False
    return copied
