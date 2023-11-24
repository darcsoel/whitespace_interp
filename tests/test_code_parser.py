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
def test_parse_tokens_for_positive_number_push(whitespace_code, tokens):
    parser = WhitespaceParser(whitespace_code)
    assert parser.process() == tokens


@pytest.mark.parametrize(
    "code, tokens",
    [
        (
            "   \t\n   \t \n   \t\t\n \t  \t \n\t\n \t\n\n\n",
            [
                "stack_push",
                "01",
                "stack_push",
                "010",
                "stack_push",
                "011",
                "stack_copy",
                "010",
                "stack_pop_number",
                "end",
            ],
        ),
        (
            "   \t\n   \t \n   \t\t\n \t  \t\n\t\n \t\n\n\n",
            [
                "stack_push",
                "01",
                "stack_push",
                "010",
                "stack_push",
                "011",
                "stack_copy",
                "01",
                "stack_pop_number",
                "end",
            ],
        ),
        (
            "   \t\n   \t \n   \t\t\n \t\n\t\t     \n\t\n \t\n\n\n",
            [
                "stack_push",
                "01",
                "stack_push",
                "010",
                "stack_push",
                "011",
                "stack_slide_n_top_off",
                "1100000",
                "stack_pop_number",
                "end",
            ],
        ),
    ],
)
def test_stack_operations(code, tokens):
    parser = WhitespaceParser(code)
    parsed_tokens = parser.process()
    assert parsed_tokens == tokens


@pytest.mark.parametrize(
    "code, tokens",
    [
        ("  \t\n\t\n \t\n\n\n", ["stack_push", "1", "stack_pop_number", "end"]),
        (
            "   \t\n   \t \n   \t\t\n \t \t\t\n\t\n \t\n\n\n",
            [
                "stack_push",
                "01",
                "stack_push",
                "010",
                "stack_push",
                "011",
                "stack_copy",
                "11",
                "stack_pop_number",
                "end",
            ],
        ),
    ],
)
def test_stack_edge_cases(code, tokens):
    parser = WhitespaceParser(code)
    assert parser.process() == tokens


@pytest.mark.parametrize(
    "code, tokens",
    [
        (
            "  \t\t\n   \t  \n\t   \t\n \t\n\n\n",
            ["stack_push", "11", "stack_push", "0100", "add", "stack_pop_number", "end"],
        ),
        (
            "  \t\t \n   \t  \n\t  \t\t\n \t\n\n\n",
            ["stack_push", "110", "stack_push", "0100", "subsctract", "stack_pop_number", "end"],
        ),
    ],
)
def test_arithmetic(code, tokens):
    parser = WhitespaceParser(code)
    parsed_tokens = parser.process()
    assert parsed_tokens == tokens
