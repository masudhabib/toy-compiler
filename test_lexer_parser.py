import pytest
from lexer import Lexer
from parser import Parser


def f(text_input):
    lexer = Lexer().get_lexer()
    tokens = lexer.lex(text_input)

    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    parser.parse(tokens).eval()


def test_evaluation(capfd):
    text_input = """
    print(4 + 4 - 20);
    """
    f(text_input)
    out, err = capfd.readouterr()
    print(out)
    print(err)
    assert out == "-12\n"



