import re
from typing import Any, Union

from imps import (
    AbstractImps,
    ArithmeticImps,
    HeapAccessImps,
    IoControlImps,
    IoImps,
    StackManipulationImps,
)


# to help with debugging
def unbleach(n: str) -> str:
    return n.replace(" ", "s").replace("\t", "t").replace("\n", "n")


class WhitespaceParser:
    keywords = {" ", "\n", "\t"}

    tokens_representation = {
        # stack
        "  ": "stack_push",  # parameter
        " \n ": "stack_duplicate",
        " \t ": "stack_copy",  # parameter
        " \n\t": "stack_swap_top_two",
        " \n\n": "stack_discard_top",
        " \t\n": "stack_slide_n_top_off",  # parameter
        # arithmetic
        "\t   ": "add",
        "\t  \t": "subsctract",
        "\t  \n": "multiplication",
        "\t  \t ": "integer_division",
        "\t \t\t": "modulo",
        "\t\t ": "store_in__heap",
        "\t\t\t": "retrieve_from_heap",
        # input-output
        "\n  ": "mark_location",
        "\n \t": "call_subrt",
        "\n \n": "jump",
    }

    def __init__(self, code: str) -> None:
        self._code = code
        self._code_shadow = code

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
        start_index, end_index = 0, 1
        tokens = []

        while end_index <= len(code):
            for imp, executor_class in self.imps.items():
                if code[start_index:end_index].startswith(imp):
                    executor = executor_class(code, start_index, end_index)
                    # executor.check_token()
                    tokens.append(next(executor.process()))
                else:
                    end_index += 1

        return tokens


class WhitespaceInterpreter:
    def __init__(self, tokens: list[str]) -> None:
        self._tokens = tokens

    def execute(self):
        return "0"


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
