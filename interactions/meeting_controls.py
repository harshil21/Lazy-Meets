import pyautogui as gui
import logging

from helpers.get_location import get_button_location

from time import sleep


def leave_meeting() -> None:
    l_coords = get_button_location("icons/leave_button", region=(0, 49, 1919, 74))
    if l_coords is None:
        raise ValueError("Could not find leave button location!")
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
