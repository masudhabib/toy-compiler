import pytest
from lexer import Lexer
from parser import Parser
from codegen import CodeGen


def f(text_input):
    lexer = Lexer().get_lexer()
    tokens = lexer.lex(text_input)
    
    codegen = CodeGen()
    module = codegen.module
    builder = codegen.builder
    printf = codegen.printf
    pg = Parser(module, builder, printf)
    pg.parse()
    
    parser = pg.get_parser()
    parser.parse(tokens).eval()


def test_valid_evaluation():
    """
    Test with valid parsing text
    """
    f("print(4 + 4 - 20);")

    f("print(5 - 4);")
    
def test_invalid_evaluation():
    """
    Test with invalid parsing text
    """
    with pytest.raises(Exception) as e:
        f("print(5 + - 4);")

    # missing ending semi colon
    with pytest.raises(Exception) as e:
        f("print(5 - 4)")


