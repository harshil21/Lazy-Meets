import argparse

import pytest

from interactions.arg_parser import parse_cmd


@pytest.fixture(scope='session')
def parser() -> argparse.ArgumentParser:
    return parse_cmd()


@pytest.mark.parametrize("args,output", [([], 'info'), (['-l', 'debug'], 'debug'), 
                                        (['--level'], None), 
                                        (['-l', 'info', '--level', 'debug'], 'debug')])
def test_arg_parse(parser, args, output):
    namespace = parser.parse_args(args)
    assert namespace.level == output


@pytest.mark.parametrize("args,output", [(['--wrong'], None)])
def test_wrong_arg_parse(parser, args, output):
    with pytest.raises(SystemExit) as e:
        parser.parse_args(args)