import pytest
import sys
sys.path.insert(0,'..')
from lexer import Lexer
from parser import Parser


def setup(text_input):
    lexer = Lexer().get_lexer()
    tokens = lexer.lex(text_input)

    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    parser.parse(tokens).eval()


def test_evaluation(capfd):
    setup("""
    print(4 + 4 - 2);
    """)
    out, err = capfd.readouterr()
    assert out == "6"



