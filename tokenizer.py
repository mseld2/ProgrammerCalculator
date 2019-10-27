from token_type import TokenType
import collections
import re
from number import Number

Token = collections.namedtuple('Token', ['type', 'value'])

class Tokenizer(object):
    ''''
    Tokenizer for programmer calculator
    See: https://docs.python.org/3/library/re.html (Writing a Tokenizer)

    Expected format for numbers
    Decimal: \b([0-9]+) 
        Examples: 120, 290, 01
    Binary: \b(b[0-1]+)
        Examples: b10101 b001
    Hex: \b(x[a-fA-F0-9]+)
        Examples: xae99 x19ed x00FF
    Octal: \b(o[0-7]+)
        Examples: o1764 o001
    '''

    def __init__(self, expr):
        self.expr = expr
        self._tokenDefinitions = [
            (TokenType.BINARY.name, r'\b(b[0-1]+)'),
            (TokenType.HEX.name, r'\b(x[a-fA-F0-9]+)'),
            (TokenType.OCTAL.name, r'\b(o[0-7]+)'),
            (TokenType.DECIMAL.name, r'\b([0-9]+)'),
            (TokenType.LPAREN.name, r'\('),
            (TokenType.RPAREN.name, r'\)'),
            (TokenType.INVERT.name, r'~'),
            (TokenType.MULTIPLY.name, r'\*'),
            (TokenType.DIVIDE.name, r'\/\/'),
            (TokenType.REMAINDER.name, r'%'),
            (TokenType.ADD.name, r'\+'),
            (TokenType.MINUS.name, r'-'),
            (TokenType.LSHIFT.name, r'\<\<'),
            (TokenType.RSHIFT.name, r'\>\>'),
            (TokenType.AND.name, r'\&'),
            (TokenType.XOR.name, r'\^'),
            (TokenType.OR.name, r'\|'),
            (TokenType.SKIP.name, r'[ \t]+'),
            (TokenType.ERROR.name, r'.')
        ]

    def tokenize(self):
        tokenRegex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in self._tokenDefinitions)
        for match in re.finditer(tokenRegex, self.expr):
            kind = match.lastgroup
            value = match.group()
            position = match.start()
            tokenTypeKind = TokenType[kind]
            if tokenTypeKind == TokenType.SKIP:
                continue
            elif tokenTypeKind == TokenType.HEX or tokenTypeKind == TokenType.OCTAL or tokenTypeKind == TokenType.BINARY:
                value = f'0{value}'
            elif TokenType[kind] == TokenType.ERROR:
                raise RuntimeError(f'Unexpected value {value} at position {position}')

            yield Token(TokenType[kind], value)


