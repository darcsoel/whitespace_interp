import pytest

from interpreter import WhitespaceInterpreter


@pytest.mark.parametrize("binary, integer", [("01", 1), ("11", -1), ("011", 3)])
def test_convert_binary_to_int(binary, integer):
    assert WhitespaceInterpreter.binary_to_number(binary) == integer


@pytest.mark.parametrize("binary, char", [("01000001", "A"), ("01001000", "H")])
def test_convert_binary_to_char(binary, char):
    assert WhitespaceInterpreter.binary_to_char(binary) == char
