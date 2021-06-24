import subprocess
from re import sub

import pytest

from get_clipboard import get_clipboard_content, purge_clipboard_contents, call_clipboard_cmd


@pytest.mark.parametrize("copied,expected", [('text (420) text', '420'), ('num 21', '21'), ('just text', None)])
def test_get_clipboard_content(copied, expected):
    # run powershell -h to know how to pass args to powershell via cmd. 
    cmd = 'powershell -Command "& {Set-Clipboard -Value \'{_}\'}'.replace('_', copied)
    subprocess.run(cmd, shell=True)
    assert get_clipboard_content() == expected 


def test_purge_clipboard_contents():
    copied = call_clipboard_cmd()
    assert copied
    purge_clipboard_contents()
    assert not call_clipboard_cmd()
    
