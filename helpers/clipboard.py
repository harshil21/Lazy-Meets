import re
import logging
import subprocess

from typing import Optional


def get_clipboard_content() -> Optional[str]:
    """Fetches the first copied item from clipboard and returns the last number if found."""
    clipboard = subprocess.run(['powershell', '-Command', 'Get-Clipboard'], stdout=subprocess.PIPE)
    copied = clipboard.stdout.decode().strip()
    num = re.search(r"\d+", copied)
    return num.group() if num else None


def purge_clipboard_contents() -> None:
    subprocess.run(["powershell", "-Command", "scb"])
    logging.debug('purging clipboard')


def insert_into_clipboard() -> None:
    subprocess.run(['powershell', "-Command", "Set-Clipboard -Value 'In this Meeting (2)'"])
