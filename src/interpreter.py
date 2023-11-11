class WhitespaceInterpreter:
    """
    Receives tokens and builds AST from them.
    """

    def __init__(self, tokens: list[str]) -> None:
        # linked list looks like more proper structure
        # made with list to simplify things
        self._tokens = tokens

        self._stack: list[str] = []
        self._heap: dict[str, str] = {}

    @staticmethod
    def binary_to_number(value: str) -> int:
        """
        Parse binary to decimal.

        Args:
            value (str): binary representation, ex 0101

        Raises:
            ValueError: in case of empty input

        Returns:
            int: parsed integer base 10
        """

        if not value:
            raise ValueError("Not valid number. Number could not contain only LF symbol.")

        if len(value) == 1:
            return 0

        sign = 1 if value[0] == "0" else -1
        return sign * int(value[1:], 2)

    @staticmethod
    def binary_to_char(value: str) -> str:
        if not value:
            return ""

        return chr(int(value, 2))

    def execute(self) -> str:

        for token in self._tokens:
            pass

        return "1"
