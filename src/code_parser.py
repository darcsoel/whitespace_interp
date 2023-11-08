from dataclasses import dataclass
from typing import Any, Optional, Union


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
        "  ": "stack_push",  # number
        " \n ": "stack_duplicate",
        " \t ": "stack_copy",  # number
        " \n\t": "stack_swap_top_two",
        " \n\n": "stack_discard_top",
        " \t\n": "stack_slide_n_top_off",  # number
        # arithmetic
        "\t   ": "add",
        "\t  \t": "subsctract",
        "\t  \n": "multiplication",
        "\t  \t ": "integer_division",
        "\t \t\t": "modulo",
        # heap access
        "\t\t ": "store_in__heap",
        "\t\t\t": "retrieve_from_heap",
        # flow control
        "\n  ": "mark_location",  # label
        "\n \t": "call_subrt",  # label
        "\n \n": "jump",  # label
        "\n\t ": "jump_if_zer",  # label,
        "\n\t\t": "jump_if_neg",  # label
        "\n\t\n": "end_subr",
        "\n\n\n": "end",
        # IO
        "\t\n  ": "stack_pop_char",
        "\t\n \t": "stack_pop_number",
        "\t\n\t ": "read_char_stack_push",
        "\t\n\t\t": "read_num_stack_push",
    }

    tokens_with_param: dict[str, str] = {
        "stack_push": "number",
        "stack_copy": "number",
        "stack_slide_n_top_off": "number",
        "mark_location": "label",
        "call_subrt": "label",
        "jump": "label",
        "jump_if_zer": "label",
        "jump_if_neg": "label",
    }

    label = r"[\t\s][\s\t]+\n"

    def __init__(self, code: str) -> None:
        self._code = code

        self._stack: list[Union[str, int]] = []
        self._heap: dict[str, Any] = {}

        self._tokens: list[str] = []

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

        return InputValueToken(value="".join(binary_representation), length=len(binary_representation) + 1)

    def process(self) -> list[str | int]:
        code_string = self.remove_comments_from_code()
        start_index = 0
        tokens: list[str | int] = []

        while start_index < len(code_string):
            for code, token in self.tokens_representation.items():
                if self._code[start_index:].startswith(code):
                    tokens.append(token)
                    shift = len(code)

                    if next_action := self.tokens_with_param.get(token):
                        if next_action == "number":
                            if number_token := self.parse_input(code_string[start_index + shift :]):
                                tokens.append(number_token.value)
                                shift += number_token.length

                        elif next_action == "label":
                            # if label_token := self.parse_label(code_string[start_index + shift :]):
                            #     tokens.append(label_token.value)
                            #     shift += label_token.length
                            pass
                        else:
                            continue

                    start_index += shift

        return tokens
