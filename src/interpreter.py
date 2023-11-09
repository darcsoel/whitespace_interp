# pylint: disable=too-few-public-methods


class WhitespaceInterpreter:
    """
    Receives tokens and builds AST.
    """

    def __init__(self, tokens: list[str]) -> None:
        self._tokens = tokens
        self._stack: list[str] = []
        self._heap: dict[str, str] = {}

    def execute(self) -> str:
        return []
