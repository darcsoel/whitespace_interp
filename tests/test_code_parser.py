from code_parser import NumberToken, WhitespaceParser


def test_binary_positive_number_parser() -> None:
    number = " \t\n"
    parsed = WhitespaceParser.parse_number(number)
    assert parsed == NumberToken(value=1, length=3)


def test_binary_positive_number_with_code_behind() -> None:
    number = " \t\n\t\n \t\n\n\n"
    parsed = WhitespaceParser.parse_number(number)
    assert parsed == NumberToken(value=1, length=3)


def test_binary_negative_number_parser() -> None:
    number = "\t\t\n"
    parsed = WhitespaceParser.parse_number(number)
    assert parsed == NumberToken(value=-1, length=3)


def test_label_parser():
    label = ""
    parsed = WhitespaceParser.parse_label(label)
