import argparse


def parse_cmd() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='A script which automatically leaves a MS Teams meeting when you\'re not around.')

    parser.add_argument('-l', '--level', help='sets the logging level', nargs='?',
                        choices=['debug', 'info', 'warning', 'exception', 'error', 'critical'],
                        default='info')
    return parser
