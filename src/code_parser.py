from dataclasses import dataclass
from typing import Any, Optional, Union

from commands import WhitespaceTokens


@dataclass
class InputValueToken:
    """
    Entity for number
    """

    value: str
    length: int


class WhitespaceParser:
    """
    Parse code into tokens.

    """

    keywords = {" ", "\n", "\t"}

    tokens_representation: dict[str, str] = {
        # stack
        "  ": WhitespaceTokens.STACK_PUSH,  # number
        " \n ": WhitespaceTokens.STACK_DUPLICATE,
        " \t ": WhitespaceTokens.STACK_COPY,  # number
        " \n\t": WhitespaceTokens.STACK_SWAP,
        " \n\n": WhitespaceTokens.STACK_DISCARD_TOP,
        # remove top N below the stack top value
        " \t\n": WhitespaceTokens.STACK_SLIDE_N_TOP_OFF,  # number
        # arithmetic: pop top two  from stack, then do the math
        "\t   ": WhitespaceTokens.ADD,
        "\t  \t": WhitespaceTokens.SUBSCTRACT,
        "\t  \n": WhitespaceTokens.MUPLITIPLICATION,
        "\t  \t ": WhitespaceTokens.INTEGER_DIVISION,
        "\t \t\t": WhitespaceTokens.MODULO,
        # heap access
        "\t\t ": WhitespaceTokens.HEAP_STORE,  # pop a and b, store a at heap address b
        "\t\t\t": WhitespaceTokens.HEAP_RETRIEVE,
        # flow control
        "\n  ": WhitespaceTokens.MARK_LOCATION,  # label
        "\n \t": WhitespaceTokens.CALL_SUBROUTINE,  # label
        "\n \n": WhitespaceTokens.JUMP,  # label
        "\n\t ": WhitespaceTokens.JUMP_IF_ZERO,  # label,
        "\n\t\t": WhitespaceTokens.JUMO_IF_NEG,  # label
        "\n\t\n": WhitespaceTokens.END_SUBROUTINE,
        "\n\n\n": WhitespaceTokens.END,
        # IO
        "\t\n  ": WhitespaceTokens.STACK_POP_CHAR,
        "\t\n \t": WhitespaceTokens.STACK_POP_NUMBER,
        "\t\n\t ": WhitespaceTokens.READ_CHAR_STACK_PUSH,
        "\t\n\t\t": WhitespaceTokens.READ_NUMBER_STACK_PUSH,
    }

    tokens_with_param: dict[str, str] = {
        WhitespaceTokens.STACK_PUSH: "number",
        WhitespaceTokens.STACK_COPY: "number",
        WhitespaceTokens.STACK_SLIDE_N_TOP_OFF: "number",
        WhitespaceTokens.MARK_LOCATION: "label",
        WhitespaceTokens.CALL_SUBROUTINE: "label",
        WhitespaceTokens.JUMP: "label",
        WhitespaceTokens.JUMP_IF_ZERO: "label",
        WhitespaceTokens.JUMO_IF_NEG: "label",
    }

    label = r"[\t\s][\s\t]+\n"

    def __init__(self, code: str) -> None:
        self._code = code

        self._stack: list[Union[str, int]] = []
        self._heap: dict[str, Any] = {}

    def remove_comments_from_code(self) -> str:
        without_comments = []

        for char in self._code:
            if char in self.keywords:
                without_comments.append(char)

        return "".join(without_comments)

    @staticmethod
    def parse_input(code: str) -> Optional[InputValueToken]:
        if not code:
            return None

        binary_representation: list[str] = []

        for char in code:
            if char == "\n":
                break

            if char == " ":
                binary_representation.append("0")
            elif char == "\t":
                binary_representation.append("1")

        # length - token len + end symbol
        return InputValueToken(value="".join(binary_representation), length=len(binary_representation) + 1)

    def process(self) -> list[str]:
        code_string = self.remove_comments_from_code()
        start_index = 0
        tokens: list[str] = []

        while start_index < len(code_string):
            for code, token in self.tokens_representation.items():
                if self._code[start_index:].startswith(code):
                    tokens.append(token)
                    shift = len(code)

                    if next_action := self.tokens_with_param.get(token):
                        if next_action in {"number", "label"}:
                            if number_token := self.parse_input(code_string[start_index + shift :]):
                                tokens.append(number_token.value)
                                shift += number_token.length

                        else:
                            continue

                    start_index += shift

        return tokens
