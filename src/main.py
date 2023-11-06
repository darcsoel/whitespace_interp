import re
from typing import Any, Union


# to help with debugging
def unbleach(n: str) -> str:
    return n.replace(" ", "s").replace("\t", "t").replace("\n", "n")


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
        "\t\n  ": "stack_pop",
        "\t\n \t": "stack_pop_n",
        "\t\n\t ": "read_char_stack_push",
        "\t\n\t\t": "read_num_stack_push",
    }

    tokens_with_param: set[str] = {
        "stack_push",
        "stack_copy",
        "stack_slide_n_top_off",
        "mark_location",
        "call_subrt",
        "jump",
        "jump_if_zer",
        "jump_if_neg",
    }

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

    def process(self) -> list[str]:
        code = self.remove_comments_from_code()
        start_index = 0
        tokens = []

        while start_index < len(code):
            for code, token in self.tokens_representation.items():
                if self._code[start_index:].startswith(code):
                    tokens.append(token)
                    start_index += len(token)

        return tokens


class WhitespaceInterpreter:
    """
    Receives tokens and builds AST.
    """

    def __init__(self, tokens: list[str]) -> None:
        self._tokens = tokens

    def execute(self):
        pass


# solution
# function, because of auto tests
def whitespace(code: str, inp: str = "") -> str:
    #  "   \t\n\t\n \t\n\n\n"
    # first 2 spaces - push to stack command
    # after that - space+\t\n - binary number (1)
    # space after - push to the stack top (\t\n \t)

    processor = WhitespaceParser(code)
    tokens = processor.process()

    interpreter = WhitespaceInterpreter(tokens)
    return interpreter.execute()
