import sys
import logging


def check(signum, frame):
    try:
        input(f'press any key to resume or ctrl-c again to terminate! ')
    except EOFError as e:  # when ctrl c is pressed while in input()
        print()
        logging.warning("program exit!")
        sys.exit(0)
