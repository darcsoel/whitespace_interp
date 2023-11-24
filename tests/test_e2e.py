# pylint:disable=missing-module-docstring

import pytest

from main import whitespace


@pytest.mark.parametrize(
    "code, result",
    [
        ("   \t\n\t\n \t\n\n\n", "1"),
        ("   \t \n\t\n \t\n\n\n", "2"),
        ("   \t\t\n\t\n \t\n\n\n", "3"),
        ("    \n\t\n \t\n\n\n", "0"),
    ],
)
def test_positive_number(code, result):
    # first pair explanation
    # stack push
    # binary 1
    # stack pop number
    # end
    assert whitespace(code) == result


@pytest.mark.parametrize(
    "code, result",
    [("  \t\t\n\t\n \t\n\n\n", "-1"), ("  \t\t \n\t\n \t\n\n\n", "-2"), ("  \t\t\t\n\t\n \t\n\n\n", "-3")],
)
def test_negative_number(code, result):
    assert whitespace(code) == result


@pytest.mark.parametrize(
    "code, result",
    [("   \t     \t\n\t\n  \n\n\n", "A"), ("   \t    \t \n\t\n  \n\n\n", "B"), ("   \t    \t\t\n\t\n  \n\n\n", "C")],
)
def test_label(code, result):
    # first pair explanation
    # stack push
    # A letter
    # pop char from stack
    # end

    assert whitespace(code) == result


@pytest.mark.parametrize(
    "code, result",
    [
        ("sadaqefdgdgdfgf   \t     \t\n\t\n  \n\n\n", "A"),
        ("dfgdgrtretbcbvcb   \t    \t \n\t\n  \n\n\n", "B"),
        ("asddqqebcvbcvb   \t    \t\t\n\t\n  \n\n\n", "C"),
    ],
)
def test_label_with_comments(code, result):
    # first pair explanation
    # stack push
    # A letter
    # pop char from stack
    # end

    assert whitespace(code) == result


@pytest.mark.parametrize(
    "code, result",
    [
        ("   \t\n   \t \n   \t\t\n \t  \t \n\t\n \t\n\n\n", "1"),
        ("   \t\n   \t \n   \t\t\n \t   \n\t\n \t\n\n\n", "3"),
        ("   \t\n   \t \n   \t\t\n \t\n\t\t     \n\t\n \t\n\n\n", "3"),
        ("  \t\n\t\n \t\n\n\n", "0"),
    ],
)
def test_stack_operations(code, result):
    assert whitespace(code) == result


# scenarios:
# copy index with negative index, index out of bounds
@pytest.mark.parametrize("code", [("   \t\n   \t \n   \t\t\n \t \t\t\n\t\n \t\n\n\n")])
def test_stack_edge_cases(code):
    with pytest.raises(ValueError):
        whitespace(code)


@pytest.mark.parametrize(
    "code, result",
    [("  \t\t\n   \t  \n\t   \t\n \t\n\n\n", "3"), ("  \t\t \n   \t  \n\t  \t\t\n \t\n\n\n", "-6")],
)
def test_arithmetic_operations(code, result):
    assert whitespace(code) == result
