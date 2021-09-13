from typing import Tuple
import logging

import pyautogui as gui

from helpers.clipboard import get_clipboard_content
from helpers.copy_methods import copy_trier
from interactions.meeting_controls import close_participants_tab, open_participants_tab
from helpers.get_location import get_button_location


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
    pane_region = (1520, 125, 399, 950)
    i_x = i_y = p_x = p_y = None

    i_coords = get_button_location("icons/participants_list", region=i_region)

    if i_coords is None:
        raise ValueError("Could not find participants list button location!")
    i_x, i_y = i_coords
    open_participants_tab(i_x, i_y)

    # Locate the number of participants in that pane.
    p_coords = get_button_location("icons/participants_number", region=pane_region, bt_region=True)

    if p_coords is None:
        raise ValueError("Could not find participants string location!")

    copy_trier(tab_close=i_coords, string_region=p_coords)  # Try to copy participant info

    try:
        copied_string = get_clipboard_content()
    except Exception as e:
        logging.error(f"Exception raised: {e}.")
    else:
        copied_number = copied_string
        close_participants_tab(i_x, i_y)  # Finish up by closing the tab

        return int(copied_number)
