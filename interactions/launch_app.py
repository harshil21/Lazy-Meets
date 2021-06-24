import pyautogui as gui


def launch_teams():
    """Launches MS Teams from your system, if not launched. If it's already
    opened, then it'll bring it into focus."""

    gui.press("win")  # Press windows key to start searching
    gui.write("Microsoft Teams")  # Search for Microsoft Teams
    gui.press("enter")  # Enter to launch!
