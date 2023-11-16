import pytest

from code_parser import InputValueToken, WhitespaceParser


@pytest.mark.parametrize(
    "whitespace_code, token",
    [
        (" \t\n", InputValueToken(value="01", length=3)),
        (" \t\n\t\n \t\n\n\n", InputValueToken(value="01", length=3)),
        ("\t\t\n", InputValueToken(value="11", length=3)),
    ],
)
def test_binary_positive_number_parser(whitespace_code, token):
    assert WhitespaceParser.parse_input(whitespace_code) == token


def test_label_parser():
    label = " \t     \t\n"
    parsed = WhitespaceParser.parse_input(label)
    assert parsed == InputValueToken(value="01000001", length=9)


@pytest.mark.parametrize(
    "whitespace_code, tokens",
    [
        ("   \t\n\t\n \t\n\n\n", ["stack_push", "01", "stack_pop_number", "end"]),
        ("   \t \n\t\n \t\n\n\n", ["stack_push", "010", "stack_pop_number", "end"]),
        ("   \t     \t\n\t\n  \n\n\n", ["stack_push", "01000001", "stack_pop_char", "end"]),
    ],
)
def test_parse_tokens_for_positive_number_1_push(whitespace_code, tokens):
    parser = WhitespaceParser(whitespace_code)
    assert parser.process() == tokens
