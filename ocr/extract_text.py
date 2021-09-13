try:
    import pytesseract
except ImportError as e:
    raise ImportError("You haven't installed pytesseract, can't get participant number! "
                      "Check https://github.com/harshil21/Lazy-Meets#installing-pytesseract-&-google-tesseract"
                      " on how to install")
import os

from helpers.clipboard import insert_into_clipboard

if os.name == 'nt':
    path = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"  # default location to install pytesseract
    pytesseract.pytesseract.tesseract_cmd = path


def do_ocr(_: int = None, y: int = None):
    """Perform OCR on image to retrieve number of ppl in meeting. The arguments are not necessary."""
    text = pytesseract.image_to_string('ocr_participant.png', lang='eng').strip()
    insert_into_clipboard(text)
    return bool(text)
