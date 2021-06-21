from tkinter import Tk
import re
import subprocess

from typing import Optional


def get_clipboard_content() -> Optional[str]:
    root = Tk()
    root.withdraw()
    clipboard = root.clipboard_get()
    num = re.search(r"\d+", clipboard)
    return num.group() if num else None


def purge_clipboard_contents() -> None:
    subprocess.run(["powershell", "-Command", "scb"])    
