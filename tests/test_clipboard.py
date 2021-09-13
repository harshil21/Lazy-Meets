import subprocess

import pytest

from helpers.clipboard import get_clipboard_content, purge_clipboard_contents


@pytest.mark.parametrize("copied,expected", [('num 21', '21'), ('just text', None), ('text (420) text', '420')])
def test_get_clipboard_content(copied, expected):
    # run powershell -h to know how to pass args to powershell via cmd. 
    cmd = 'powershell -Command "& {Set-Clipboard -Value \'{_}\'}'.replace('_', copied)
    subprocess.run(cmd, shell=True)
    assert get_clipboard_content() == expected 


def test_purge_clipboard_contents():
    copied = get_clipboard_content()
    assert copied
    purge_clipboard_contents()
    assert not get_clipboard_content()
    
