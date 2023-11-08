from code_parser import WhitespaceParser
from interpreter import WhitespaceInterpreter


# to help with debugging
def unbleach(n: str) -> str:
    return n.replace(" ", "s").replace("\t", "t").replace("\n", "n")


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
