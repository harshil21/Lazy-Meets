import time

import pyautogui as gui
from pygetwindow import PyGetWindowException

from get_coords import get_participant_number
from meeting_controls import leave_meeting


gui.PAUSE = 0.2  # Failsafe - 0.2 seconds to abort program by moving cursor to any corner.


def maximize_screen():
    windows = gui.getWindowsWithTitle("Microsoft Teams")
    windows[0].maximize()
    windows[0].activate()


def main() -> None:
    new = None
    while True:
        try:
            initial = new if new is not None else 0

            if initial:
                print(f"sleeping for 40s")
                time.sleep(40)

            maximize_screen()
            new = get_participant_number()
            print(f"Difference in members {new-initial}")

            if new - initial <= -7:  # If 7 or more people left, stop.
                print("quitting cause everyone is leaving!")
                leave_meeting()
                break

        except KeyboardInterrupt:
            print("exiting loop!")
            break

        except gui.FailSafeException:
            print("program aborted due to user intervention!")
            break

        except ValueError as e:
            print(e)
            time.sleep(40)

        except (IndexError, PyGetWindowException):
            print("Meeting has closed/ended.")
            break


if __name__ == "__main__":
    main()
