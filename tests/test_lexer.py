import pytest
from lexer import Lexer

def f(text_input):
    lexer = Lexer().get_lexer()
    tokens = lexer.lex(text_input)
    for t in tokens:
        print(t)

def test_single_token(capfd):
    f("4")
    out, err = capfd.readouterr()
    assert out == "Token('NUMBER', '4')\n"

    f("+")
    out, err = capfd.readouterr()
    assert out == "Token('SUM', '+')\n"
    
    f("(")
    out, err = capfd.readouterr()
    assert out == "Token('OPEN_PAREN', '(')\n"


def test_multiple_tokens(capfd):
    f("4 + 100")
    out, err = capfd.readouterr()
    #assert out == "Token('NUMBER', '4')\nToken('SUM', '+')\nToken('NUMBER', '100')\n"
    assert out=="\n".join(["Token('NUMBER', '4')","Token('SUM', '+')","Token('NUMBER', '100')\n"])


def test_negative_token(capfd):
    f("-12")
    out, err = capfd.readouterr()
    assert out == "Token('SUB', '-')\nToken('NUMBER', '12')\n"

def test_invalid_token(capfd):
    f("100                ")
    out, err = capfd.readouterr()
    assert out == "Token('NUMBER', '100')\n"

    # test with non number
    with pytest.raises(Exception) as e:
        f("100xlkf")
    
