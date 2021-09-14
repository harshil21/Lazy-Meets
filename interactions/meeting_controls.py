import pyautogui as gui
from pyautogui import Window
import logging

from helpers.location import get_button_location

from time import sleep


def leave_meeting(window: Window) -> None:
    l_coords = get_button_location("icons/leave_button", region=(0, 49, 1919, 74))
    if l_coords is None:
        logging.warning("Could not find leave button location! Attempting to force quit...")
        window.close()
        if window.isActive:  # There can be a confirmation box telling if you want to leave
            leave_confirm_coords = get_button_location("icons/confirm_leave")

            if leave_confirm_coords is None:
                raise ValueError("Could not find the confirmation of leave button!")
            lc_x, lc_y = leave_confirm_coords
            gui.click(lc_x, lc_y)
        return

    l_x, l_y = l_coords
    gui.click(l_x, l_y)


def close_participants_tab(x: int, y: int) -> None:
    logging.debug('attempting to close participant list')
    gui.click(x, y)
    gui.move(100, 100, 0)


def open_participants_tab(x: int, y: int) -> None:
    logging.debug('attempting to open participant list')
    gui.click(x, y)  # Click on it to view members, etc
    sleep(0.8)  # sleep to let the list render
