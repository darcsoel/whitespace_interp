# to help with debugging
def unbleach(n: str) -> str:
    return n.replace(" ", "s").replace("\t", "t").replace("\n", "n")


imps = {"stack_manipulation": " ", "arithmetic": "\t ", "heap_access": "\t\t", "io": "\t\n", "flow_control": "\n"}

numbers = {
    "positive": r"\s[\s\t]*\n",
    "negative": r"\t[\s\t]*\n",
}

labels = r"[\s\t]+\n"


# solution
def whitespace(code: str, inp: str = "") -> str:
    output: str = ""
    stack: list = []
    heap: dict = {}

    return output
