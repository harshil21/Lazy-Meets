import pyautogui as gui

import time
import logging

from .clipboard import get_clipboard_content
from interactions.meeting_controls import close_participants_tab, open_participants_tab
from helpers.screengrab import grab_screenshot
from ocr.extract_text import do_ocr

selected_method = None


def hotkey(x: int, y: int) -> bool:
    """Try to copy by dragging over the string, and then use hotkey."""
    gui.moveTo(x + 15, y, 0)
    gui.mouseDown()
    gui.move(70, 0)
    gui.hotkey("ctrl", "c")
    gui.mouseUp()
    return check_copied()


def drag_right_click(x: int, y: int) -> bool:
    """Try to copy by dragging over the string, then right click to copy"""
    gui.moveTo(x + 15, y, 0)
    gui.mouseDown()
    gui.move(70, 0)
    gui.mouseUp()
    gui.click(button="right")
    gui.move(10, 10)
    gui.click()
    return check_copied()


def triple_click_right_click(_: int = None, y: int = None) -> bool:
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


def copy_trier(tab_close: tuple, string_region: tuple = None) -> None:
    """
    Tries to copy the participant number (Microsoft can be troublesome)
    Args:
        tab_close - 2 length tuple specifying coordinates of participant icon (the top bar one)
        string_region - 4 length tuple specifying the region the string (i.e 'In this meeting', 'Attendees') is located.
        """
    global selected_method

    x, y = gui.center(string_region)

    if selected_method is not None:  # If a method worked previously, use it.
        if not selected_method.__name__.startswith('do_ocr'):
            gui.moveTo(x, y)
        else:
            grab_screenshot(string_region)
        selected_method(x, y)
        return
    i_x, i_y = tab_close

    for copy_method in (hotkey, drag_right_click, triple_click_right_click, do_ocr):
        if copy_method.__name__.startswith('do_ocr'):
            grab_screenshot(string_region)
        else:
            gui.moveTo(x, y)  # Reset cursor

        if copy_method(x, y):  # If copy method worked, exit loop
            selected_method = copy_method
            break
        logging.info(f"{copy_method.__name__} failed.")
        close_participants_tab(i_x, i_y)
        time.sleep(2)
        open_participants_tab(i_x, i_y)


def check_copied() -> bool:
    """Returns True if a number was copied."""
    try:
        copied = get_clipboard_content()
    except Exception as e:
        logging.debug(str(e))
        return False
    return bool(copied)
