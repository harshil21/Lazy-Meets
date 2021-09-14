import logging

import pyautogui as gui

import os


def grab_screenshot(string_region: tuple) -> None:
    """Saves a screenshot of the current participant list string so we can do OCR only on that."""
    left, top, width, height = string_region
    gui.screenshot('ocr_participant.png', region=(left, top, width + 30, height))  # add 30 pixels to include number


def remove_screenshot():
    try:
        os.remove('ocr_participant.png')
        logging.debug('removed screenshot')
    except FileNotFoundError:
        pass
