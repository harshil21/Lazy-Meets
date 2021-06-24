import pyautogui as gui

import os
import logging


def get_button_location(path: str, region: tuple = None):
    """Tries to locate the button on screen."""
    split = path.split("/")
    for file in os.listdir(split[0]):
        if file.startswith(split[1]):
            coords = gui.locateCenterOnScreen(f"{split[0]}/{file}", region=region)
            if coords is not None:
                logging.debug(f'{file} was chosen')
                return coords[0], coords[1]
    return None
