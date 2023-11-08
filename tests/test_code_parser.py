from code_parser import InputValueToken, WhitespaceParser


def test_binary_positive_number_parser() -> None:
    number = " \t\n"
    parsed = WhitespaceParser.parse_input(number)
    assert parsed == InputValueToken(value="01", length=3)


def test_binary_positive_number_with_code_behind() -> None:
    number = " \t\n\t\n \t\n\n\n"
    parsed = WhitespaceParser.parse_input(number)
    assert parsed == InputValueToken(value="01", length=3)


def test_binary_negative_number_parser() -> None:
    number = "\t\t\n"
    parsed = WhitespaceParser.parse_input(number)
    assert parsed == InputValueToken(value="11", length=3)


def test_label_parser() -> None:
    label = " \t     \t\n"
    parsed = WhitespaceParser.parse_input(label)
    assert parsed == InputValueToken(value="01000001", length=9)
