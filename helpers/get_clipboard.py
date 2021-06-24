import re
import logging
import subprocess

from typing import Optional


def call_clipboard_cmd() -> str:
    """Runs a powershell command to get clipboard commands. Returns an empty string if clipboard is empty."""
    clipboard = subprocess.run(['powershell', '-Command', 'Get-Clipboard'], stdout=subprocess.PIPE)
    copied = clipboard.stdout.decode().strip()
    return copied


def get_clipboard_content() -> Optional[str]:
    """Fetches the first copied item from clipboard and returns the last number if found."""
    copied = call_clipboard_cmd()
    num = re.search(r"\d+", copied)
    return num.group() if num else None


def purge_clipboard_contents() -> None:
    subprocess.run(["powershell", "-Command", "scb"])
    logging.debug('purging clipboard')
