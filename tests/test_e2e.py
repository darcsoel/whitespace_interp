# pylint:disable=missing-module-docstring

from main import whitespace


def test_positive_number1():
    # stack push
    # binary 1
    # stack push number
    # end
    output = "   \t\n\t\n \t\n\n\n"
    assert whitespace(output) == "1"


def test_positive_number2():
    output = "   \t \n\t\n \t\n\n\n"
    assert whitespace(output) == "2"


def test_positive_number3():
    output = "   \t\t\n\t\n \t\n\n\n"
    assert whitespace(output) == "3"


def test_positive_number4():
    output = "    \n\t\n \t\n\n\n"
    assert whitespace(output) == "0"


def test_negative_number1():
    output = "  \t\t\n\t\n \t\n\n\n"
    assert whitespace(output) == "-1"


def test_negative_number2():
    output = "  \t\t \n\t\n \t\n\n\n"
    assert whitespace(output) == "-2"


def test_negative_number3():
    output = "  \t\t\t\n\t\n \t\n\n\n"
    assert whitespace(output) == "-3"


def test_label1():
    # stack push
    # A letter
    # pop char from stack
    # end
    output = "   \t     \t\n\t\n  \n\n\n"
    assert whitespace(output) == "A"


def test_label2():
    output = "   \t    \t \n\t\n  \n\n\n"
    assert whitespace(output) == "B"


def test_label3():
    output = "   \t    \t\t\n\t\n  \n\n\n"
    assert whitespace(output) == "C"
