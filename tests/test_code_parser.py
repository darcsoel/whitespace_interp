from code_parser import InputValueToken, WhitespaceParser


def test_binary_positive_number_parser():
    number = " \t\n"
    parsed = WhitespaceParser.parse_input(number)
    assert parsed == InputValueToken(value="01", length=3)


def test_binary_positive_number_with_code_behind():
    number = " \t\n\t\n \t\n\n\n"
    parsed = WhitespaceParser.parse_input(number)
    assert parsed == InputValueToken(value="01", length=3)


def test_binary_negative_number_parser():
    number = "\t\t\n"
    parsed = WhitespaceParser.parse_input(number)
    assert parsed == InputValueToken(value="11", length=3)


def test_label_parser():
    label = " \t     \t\n"
    parsed = WhitespaceParser.parse_input(label)
    assert parsed == InputValueToken(value="01000001", length=9)


def test_parse_tokens_for_positive_number_1_push():
    code = "   \t\n\t\n \t\n\n\n"
    parser = WhitespaceParser(code)

    assert parser.process() == ["stack_push", "01", "stack_pop_number", "end"]


def test_parse_tokens_for_positive_number_2_push():
    code = "   \t \n\t\n \t\n\n\n"
    parser = WhitespaceParser(code)

    assert parser.process() == ["stack_push", "010", "stack_pop_number", "end"]


def test_parse_tokens_for_label_a_push():
    code = "   \t     \t\n\t\n  \n\n\n"
    parser = WhitespaceParser(code)

    assert parser.process() == ["stack_push", "01000001", "stack_pop_char", "end"]
