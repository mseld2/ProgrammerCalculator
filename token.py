from enum import Enum
import re

class TokenType(Enum):
    EOF = "EOF"
    BINARY = "BINARY"
    HEX = "HEX"
    OCTAL = "OCTAL"
    DECIMAL = "DECIMAL"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    NEGATE = "NEGATE"
    INVERT = "INVERT"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    REMAINDER = "REMAINDER"
    ADD = "ADD
    SUBTRACT = "SUBTRACT"
    LSHIFT = "LSHIFT"
    RSHIFT = "RSHIFT"
    AND = "AND"
    XOR = "XOR"
    OR = "OR"
    WHITESPACE = "WHITESPACE"


class Pattern(object):
    def __init__(self):
        self.binary = r'(?P<BINARY>^0b[0-1]+$)'
        self.hex = r'(?P<HEX>^0x[a-fA-F0-9]+$)'
        self.octal = r'(?P<OCTAL>^0o[0-7]+$)'
        self.decimal = r'(?P<DECIMAL>^[1-9]{1}[0-9]+$)'
        self.rparen = r'(?P<LPAREN>\()'
        self.lparen = r'(?P<RPAREN>\))'
        self.negate = r'(?P<NEGATE>-)'
        self.invert = r'(?P<INVERT>~)'
        self.multiply = r'(?P<MULTIPLY>\*)'
        self.divide = r'(?P<DIVIDE>\/\/)'
        self.remainder = r'(?P<REMAINDER>%)'
        self.add = r'(?P<ADD>\+)'
        self.subtract = r'(?P<SUBTRACT>-)'
        self.lshift = r'(?P<LSHIFT>\<\<)'
        self.rshift = r'(?P<RSHIFT>\>\>)'
        self.ampersand = r'(?P<AND>\&)'
        self.carot = r'(?P<XOR>\^)'
        self.pipe = r'(?P<OR>\|)'
        self.whitespace = r'(?P<WHITESPACE>\s+)'

        self._value = re.compile(';'.join(self.binary, self.hex, self.octal, self.decimal, self.rparen, self.lparen, \
            self.negate, self.invert, self.multiply, self.divide, self.remainder, self.add, self.subtract, self.lshift, \
            self.rshift, self.ampersand, self.carot, self.pipe, self.whitespace))

    @property
    def value(self):
        return self._value
