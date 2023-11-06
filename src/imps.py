class AbstractImps:
    """
    Interface for Imps
    """

    def __init__(self, code: str, start_index: int, end_index: int) -> None:
        self._code = code
        self._start_index = start_index
        self._end_index = end_index


class StackManipulationImps(AbstractImps):
    """
    Stack operations: push, duplicate top, copy on the top,
    swipe two top, discard top, slide X keeping the top.
    """

    tokens_to_actions = {
        "  ": "push_to_stack",
        " \n ": "duplicate_top",
    }

    numbers = {
        "positive": r"\s[\s\t]+\n",
        "negative": r"\t[\s\t]+\n",
    }


class ArithmeticImps(AbstractImps):
    pass


class HeapAccessImps(AbstractImps):
    pass


class IoImps(HeapAccessImps):
    labels = r"[\s\t]+\n"


class IoControlImps(IoImps):
    pass
