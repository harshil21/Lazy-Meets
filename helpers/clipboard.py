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
    """Purges the all the contents in the clipboard."""
    subprocess.run(["powershell", "-Command", "scb"])
    logging.debug('purging clipboard')


def insert_into_clipboard(string) -> None:
    """Insert specified string into clipboard."""
    subprocess.run(['powershell', "-Command", f"Set-Clipboard -Value '{string}'"])
    logging.debug(f'Inserted {string} into the clipboard.')
