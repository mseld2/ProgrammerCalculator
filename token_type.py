from enum import Enum

class TokenType(Enum):
    BINARY = "BINARY"
    HEX = "HEX"
    OCTAL = "OCTAL"
    DECIMAL = "DECIMAL"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    INVERT = "INVERT"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    REMAINDER = "REMAINDER"
    ADD = "ADD"
    MINUS = "MINUS"
    LSHIFT = "LSHIFT"
    RSHIFT = "RSHIFT"
    AND = "AND"
    XOR = "XOR"
    OR = "OR"
    SKIP = "SKIP"
    ERROR = "ERROR"


