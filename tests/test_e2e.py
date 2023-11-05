# pylint:disable=missing-module-docstring

from main import whitespace


def test_positive_number1() -> None:
    output = "   \t\n\t\n \t\n\n\n"
    assert whitespace(output) == "1"


def test_positive_number2() -> None:
    output = "   \t \n\t\n \t\n\n\n"
    assert whitespace(output) == "2"


def test_positive_number3() -> None:
    output = "   \t\t\n\t\n \t\n\n\n"
    assert whitespace(output) == "3"


def test_positive_number4() -> None:
    output = "    \n\t\n \t\n\n\n"
    assert whitespace(output) == "0"


def test_negative_number1() -> None:
    output = "  \t\t\n\t\n \t\n\n\n"
    assert whitespace(output) == "-1"


def test_negative_number2() -> None:
    output = "  \t\t \n\t\n \t\n\n\n"
    assert whitespace(output) == "-2"


def test_negative_number3() -> None:
    output = "  \t\t\t\n\t\n \t\n\n\n"
    assert whitespace(output) == "-3"


def test_label1() -> None:
    output = "   \t     \t\n\t\n  \n\n\n"
    assert whitespace(output) == "A"


def test_label2() -> None:
    output = "   \t    \t \n\t\n  \n\n\n"
    assert whitespace(output) == "B"


def test_label3() -> None:
    output = "   \t    \t\t\n\t\n  \n\n\n"
    assert whitespace(output) == "C"
