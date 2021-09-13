from typing import Optional

import pyautogui as gui

import os
import logging


def get_button_location(path: str, region: tuple = None, bt_region: bool = False) -> Optional[tuple]:
    """
    Tries to locate the button on screen. Specify bt_region to return the full button region
    (left, top, width, height).
    """
    split = path.split("/")
    for file in os.listdir(split[0]):
        if file.startswith(split[1]):
            coords = gui.locateOnScreen(f"{split[0]}/{file}", region=region)

            if coords is None:
                continue

            logging.debug(f'{file} was chosen')
            if not bt_region:
                coords = gui.center(coords)
                return coords[0], coords[1]
            elif bt_region:
                return coords
