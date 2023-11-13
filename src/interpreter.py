from commands import WhitespaceTokens


class Stack:
    """
    Stack implementation.
    """

    def __init__(self) -> None:
        self._values: list[str] = []

    def pop(self) -> str:
        return self._values.pop()

    def push(self, value: str | int) -> None:
        self._values.append(str(value))

    def get(self, index: int) -> str:
        return self._values[index]


class WhitespaceInterpreter:
    """
    Receives tokens and builds AST from them.
    """

    def __init__(self, tokens: list[str]) -> None:
        # linked list looks like more proper structure
        # made with list to simplify things
        self._tokens = tokens

        self._stack = Stack()
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

    def pop_number_from_stack(self) -> int:
        """
        Pop top item from stack and convert binary -> number
        """

        return self.binary_to_number(self._stack.pop())

    def pop_character_from_stack(self) -> str:
        return self.binary_to_char(self._stack.pop())

    def execute(self) -> str:
        """
        Iterate over tokens ane execute commands represent each of them.
        """

        output = []

        for index, token in enumerate(self._tokens):
            # stack operations
            if token == WhitespaceTokens.STACK_PUSH:
                self._stack.push(self._tokens[index + 1])
            elif token == WhitespaceTokens.STACK_DUPLICATE:
                top_value = self._stack.pop()
                self._stack.push(top_value)
                self._stack.push(top_value)
            elif token == WhitespaceTokens.STACK_COPY:
                stack_item = self._stack.get(self.binary_to_number(self._tokens[index + 1]))
                self._stack.push(stack_item)
            elif token == WhitespaceTokens.STACK_SWAP:
                top1 = self._stack.pop()
                top2 = self._stack.pop()

                self._stack.push(top1)
                self._stack.push(top2)
            elif token == WhitespaceTokens.STACK_DISCARD_TOP:
                self._stack.pop()
            elif token == WhitespaceTokens.STACK_SLIDE_N_TOP_OFF:
                number = self.binary_to_number(self._tokens[index + 1])
                top_elem = self._stack.pop()

                while number:
                    self._stack.pop()
                    number -= 1

                self._stack.push(top_elem)

            # arithmetic operations
            elif token == WhitespaceTokens.ADD:
                first = self.pop_number_from_stack()
                second = self.pop_number_from_stack()
                self._stack.push(first + second)
            elif token == WhitespaceTokens.SUBSCTRACT:
                first = self.pop_number_from_stack()
                second = self.pop_number_from_stack()
                self._stack.push(second - first)
            elif token == WhitespaceTokens.MUPLITIPLICATION:
                first = self.pop_number_from_stack()
                second = self.pop_number_from_stack()
                self._stack.push(first * second)
            elif token == WhitespaceTokens.INTEGER_DIVISION:
                first = self.pop_number_from_stack()
                second = self.pop_number_from_stack()
                self._stack.push(second // first)
            elif token == WhitespaceTokens.MODULO:
                first = self.pop_number_from_stack()
                second = self.pop_number_from_stack()

                if not (modulo := second % first):
                    raise ValueError("Not valid result of modulo operation.")
                self._stack.push(modulo)

            # heap access operations
            elif token == WhitespaceTokens.HEAP_STORE:
                value = self._stack.pop()
                key = self._stack.pop()

                self._heap[key] = value
            elif token == WhitespaceTokens.HEAP_RETRIEVE:
                value = self._stack.pop()
                self._stack.push(self._heap[value])
                del self._heap[value]

            # flow control operations
            elif token == WhitespaceTokens.MARK_LOCATION:
                pass
            elif token == WhitespaceTokens.CALL_SUBROUTINE:
                pass
            elif token == WhitespaceTokens.JUMP:
                pass
            elif token == WhitespaceTokens.JUMP_IF_ZERO:
                pass
            elif token == WhitespaceTokens.JUMO_IF_NEG:
                pass
            elif token == WhitespaceTokens.END_SUBROUTINE:
                pass
            elif token == WhitespaceTokens.END:
                pass

            # IO operations
            elif token == WhitespaceTokens.STACK_POP_CHAR:
                char = self.pop_character_from_stack()
                output.append(char)
            elif token == WhitespaceTokens.STACK_POP_NUMBER:
                number = self.pop_number_from_stack()
                output.append(str(number))

        return "".join(output)
