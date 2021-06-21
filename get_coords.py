import os
from typing import Tuple
from time import sleep

import pyautogui as gui

from get_clipboard import get_clipboard_content
from copy_methods import copy_trier
from meeting_controls import close_participants_tab, open_participants_tab
from get_location import get_button_location


def get_call_channels() -> Tuple[int, int]:
    """Searches for the call in progress icon(s) in Teams channel(s)."""
    for call_in_channel in gui.locateAllOnScreen("icons/meeting_in_progress.png"):
        print(call_in_channel)
        yield gui.center(call_in_channel)  # yields x,y coords of icon.
    ...


def get_join_coords():
    """Get join meeting coords."""
    ...


def get_participant_number() -> int:
    """Gets number of participants currently in the meeting."""
    # Locate the participants icon in the screen
    i_region = (0, 49, 1919, 94)  # Region to search in (for high accuracy)
    p_region = (1520, 125, 399, 950)
    i_x = i_y = p_x = p_y = None

    i_coords = get_button_location("icons/participants_list", region=i_region)

    if i_coords is None:
        raise ValueError("Could not find participants list button location!")
    i_x, i_y = i_coords
    open_participants_tab(i_x, i_y)

    # Locate the number of participants in that pane.
    p_coords = get_button_location("icons/participants_number", region=p_region)

    if p_coords is None:
        raise ValueError("Could not find participants string location!")
    p_x, p_y = p_coords

    copy_trier(p_x, p_y, tab_close=(i_x, i_y))  # Try to copy participant info

    try:
        copied_string = get_clipboard_content()
    except Exception as e:  # Manually copy if something went wrong
        print(f"Exception raised: {e}.")
    else:
        copied_number = copied_string
        close_participants_tab(i_x, i_y)  # Finish up by closing the tab

        return int(copied_number)
