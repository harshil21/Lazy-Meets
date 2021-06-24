import argparse
import logging
import time

import pyautogui as gui
from pygetwindow import PyGetWindowException

from get_clipboard import purge_clipboard_contents
from get_coords import get_participant_number
from meeting_controls import leave_meeting
from arg_parser import parse_cmd

gui.PAUSE = 0.2  # Failsafe - 0.2 seconds to abort program by moving cursor to any corner.


def maximize_screen():
    windows = gui.getWindowsWithTitle("Microsoft Teams")
    windows[0].maximize()
    windows[0].activate()


def main() -> None:
    new = None
    purge_clipboard_contents()

    while True:
        try:
            initial = new if new is not None else 0

            if initial:
                logging.info(f"sleeping for 40s")
                time.sleep(40)

            maximize_screen()
            new = get_participant_number()
            logging.info(f"Difference in members {new-initial}. Members present are: {new}")

            if new - initial <= -7:  # If 7 or more people left, stop.
                logging.warning("quitting cause everyone is leaving!")
                leave_meeting()
                break

        except gui.FailSafeException:
            logging.warning("program aborted due to user intervention!")
            break

        except ValueError as e:
            logging.error(f'{str(e)} Sleeping for 40 seconds after error...')
            time.sleep(40)

        except (IndexError, PyGetWindowException):
            logging.warning("Meeting has closed/ended.")
            break

        purge_clipboard_contents()


if __name__ == "__main__":
    parser = parse_cmd()
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO if args.level is None else args.level.upper(),
                        format='%(name)s - %(levelname)s - %(funcName)s - %(message)s')
    logging.getLogger('PIL.PngImagePlugin').setLevel(logging.WARNING)

    try:
        main()
    except KeyboardInterrupt:
        logging.warning('program exit!')
