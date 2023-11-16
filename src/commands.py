from enum import Enum


class WhitespaceTokens(str, Enum):
    """
    Whitespace lang tokens.
    """

    STACK_PUSH = "stack_push"  # number
    STACK_DUPLICATE = "stack_duplicate_top_item"
    STACK_COPY = "stack_copy"  # number
    STACK_SWAP = "stack_swap_top_two"
    STACK_DISCARD_TOP = "stack_discard_top"
    STACK_SLIDE_N_TOP_OFF = "stack_slide_n_top_off"  # number
    # arithmetic
    ADD = "add"
    SUBSCTRACT = "subsctract"
    MUPLITIPLICATION = "multiplication"
    INTEGER_DIVISION = "integer_division"
    MODULO = "modulo"
    # heap access
    HEAP_STORE = "store_in_heap"
    HEAP_RETRIEVE = "retrieve_from_heap"
    # flow control
    MARK_LOCATION = "mark_location"  # label
    CALL_SUBROUTINE = "call_subrt"  # label
    JUMP = "jump"  # label
    JUMP_IF_ZERO = "jump_if_zer"  # label,
    JUMO_IF_NEG = "jump_if_neg"  # label
    END_SUBROUTINE = "end_subr"
    END = "end"
    # IO
    STACK_POP_CHAR = "stack_pop_char"
    STACK_POP_NUMBER = "stack_pop_number"
    READ_CHAR_STACK_PUSH = "read_char_stack_push"
    READ_NUMBER_STACK_PUSH = "read_num_stack_push"


stack_commands = {
    WhitespaceTokens.STACK_PUSH,
    WhitespaceTokens.STACK_DUPLICATE,
    WhitespaceTokens.STACK_COPY,
    WhitespaceTokens.STACK_SWAP,
    WhitespaceTokens.STACK_DISCARD_TOP,
    WhitespaceTokens.STACK_SLIDE_N_TOP_OFF,
}

arithmetic_commands = {
    WhitespaceTokens.ADD,
    WhitespaceTokens.SUBSCTRACT,
    WhitespaceTokens.MUPLITIPLICATION,
    WhitespaceTokens.INTEGER_DIVISION,
    WhitespaceTokens.MODULO,
}

heap_access_commands = {WhitespaceTokens.HEAP_STORE, WhitespaceTokens.HEAP_RETRIEVE}


flow_control_commands = {
    WhitespaceTokens.MARK_LOCATION,
    WhitespaceTokens.CALL_SUBROUTINE,
    WhitespaceTokens.JUMP,
    WhitespaceTokens.JUMP_IF_ZERO,
    WhitespaceTokens.JUMO_IF_NEG,
    WhitespaceTokens.END_SUBROUTINE,
    WhitespaceTokens.END,
}

io_commands = {
    WhitespaceTokens.STACK_POP_CHAR,
    WhitespaceTokens.STACK_POP_NUMBER,
    WhitespaceTokens.READ_CHAR_STACK_PUSH,
    WhitespaceTokens.READ_NUMBER_STACK_PUSH,
}
