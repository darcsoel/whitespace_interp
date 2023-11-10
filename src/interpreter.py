class WhitespaceInterpreter:
    """
    Receives tokens and builds AST.
    """

    def __init__(self, tokens: list[str]) -> None:
        # linked list looks like more proper structure
        # made with list to simplify things
        self._tokens = tokens

        self._stack: list[str] = []
        self._heap: dict[str, str] = {}

    @staticmethod
    def binary_to_number(value: str) -> int:
        sign = 1 if value[0] == "0" else -1
        return sign * int(value[1:], 2)

    @staticmethod
    def binary_to_char(value: str) -> str:
        return chr(int(value, 2))

    def execute(self) -> str:
        return "1"
