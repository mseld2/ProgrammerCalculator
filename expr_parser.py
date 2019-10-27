from tokenizer import Tokenizer
from tokenizer import Token
from token_type import TokenType
from number import Number

class ExprParser(object):
    '''
    Parser for grammar specified in 'language_definition.txt'
    See: https://en.wikipedia.org/wiki/Recursive_descent_parser

    Note: Need paranthesis to enforce precedence for ~ and -
        Example: ~(-b11011011) or -(~b11011011)
    '''

    def parse(self, expr):
        self.tokens = Tokenizer(expr).tokenize()
        self.currentToken = None
        self.nextToken = None
        self._nextToken()

        return self.startExpr()

    def _nextToken(self):
        self.currentToken, self.nextToken = self.nextToken, next(self.tokens, None)

    def _accept(self, tokenType):
        if self.nextToken and self.nextToken.type == tokenType:
            self._nextToken()
            return True
        else:
            return False

    def _expect(self, tokenType):
        if self._accept(tokenType):
            return True
        
        raise SyntaxError(f'Expected {tokenType.name}')

    def startExpr(self):
        '''
        L -> R
        start_expr 
            := xor_expr { '|' xor_expr }
        '''

        result = self.xorExpr()
        while self._accept(TokenType.OR):
            if self.currentToken.type != TokenType.OR:
                raise SyntaxError(f'Expected |, got {self.currentToken.value}')
            result |= self.xorExpr()
        
        return result

    def xorExpr(self):
        '''
        L -> R
        xor_expr 
            := and_expr { '^' and_expr }
        '''

        result = self.andExpr()
        while self._accept(TokenType.XOR):
            if self.currentToken.type != TokenType.XOR:
                raise SyntaxError(f'Expected ^, got {self.currentToken.value}')
            result ^= self.andExpr()
        
        return result

    def andExpr(self):
        '''
        L -> R
        and_expr 
            := shift_expr { '&' shift_expr }
        '''
        result = self.shiftExpr()
        while self._accept(TokenType.AND):
            if self.currentToken.type != TokenType.AND:
                raise SyntaxError(f'Expected &, got {self.currentToken.value}')
            result &= self.shiftExpr()
        
        return result

    def shiftExpr(self):
        '''
        L -> R
        shift_expr 
            := arith_expr { ( '<<' | '>>' ) arith_expr }
        '''

        result = self.arithExpr()
        while self._accept(TokenType.LSHIFT) or self._accept(TokenType.RSHIFT):
            if self.currentToken.type == TokenType.LSHIFT:
                result = result << self.arithExpr()
            elif self.currentToken.type == TokenType.RSHIFT:
                result = result >> self.arithExpr()
            else:
                raise SyntaxError(f'Expected >> or <<, got {self.currentToken.value}')
        
        return result

    def arithExpr(self):
        '''
        L -> R
        arith_expr
            := term { ( '+' | '-' ) term }
        '''

        result = self.term()
        while self._accept(TokenType.ADD) or self._accept(TokenType.MINUS):
            if self.currentToken.type == TokenType.ADD:
                result += self.term()
            elif self.currentToken.type == TokenType.MINUS:
                result -= self.term()
            else:
                raise SyntaxError(f'Expected + or -, got {self.currentToken.value}')           

        return result

    def term(self):
        '''
        L -> R
        term 
            := factor { ( '*' | '%' | '//' ) factor }
        '''
        result = self.factor()
        while self._accept(TokenType.MULTIPLY) or self._accept(TokenType.REMAINDER) or self._accept(TokenType.DIVIDE):
            if self.currentToken.type == TokenType.MULTIPLY:
                result *= self.factor()
            elif self.currentToken.type == TokenType.REMAINDER:
                result %= self.factor()
            elif self.currentToken.type == TokenType.DIVIDE:
                result //= self.factor()
            else:
                raise SyntaxError(f'Expected *, % or //, got {self.currentToken.value}')  
        
        return result

    def factor(self):
        '''
        L -> R
        factor 
            := ('-'|'~' ) primary | primary
        '''
        if self._accept(TokenType.MINUS):
            if self.currentToken.type != TokenType.MINUS:
                raise SyntaxError(f'Expected -, got {self.currentToken.value}')  
            return Number().fromNumber(0) - self.primary()
        elif self._accept(TokenType.INVERT):
            if self.currentToken.type != TokenType.INVERT:
                raise SyntaxError(f'Expected ~, got {self.currentToken.value}')  
            return ~self.primary()

        return self.primary()

    def primary(self):
        '''
        primary 
            := hex_number | binary_number | octal_number | decimal_number | '(' start_expr ')'
        '''

        if self._accept(TokenType.DECIMAL):
            if self.currentToken.type != TokenType.DECIMAL:
                raise SyntaxError(f'Expected decimal number, got {self.currentToken.value}')  
            return Number().fromString(self.currentToken.value)
        if self._accept(TokenType.HEX):
            if self.currentToken.type != TokenType.HEX:
                raise SyntaxError(f'Expected hex number, got {self.currentToken.value}')  
            return Number().fromString(self.currentToken.value) 
        if self._accept(TokenType.BINARY):
            if self.currentToken.type != TokenType.BINARY:
                raise SyntaxError(f'Expected binary number, got {self.currentToken.value}')  
            return Number().fromString(self.currentToken.value)
        if self._accept(TokenType.OCTAL):
            if self.currentToken.type != TokenType.OCTAL:
                raise SyntaxError(f'Expected octal number, got {self.currentToken.value}')  
            return Number().fromString(self.currentToken.value)                                     
        elif self._accept(TokenType.LPAREN):
            result = self.startExpr()

            self._expect(TokenType.RPAREN)

            return result
        else:
            raise SyntaxError(f'Got unexpected token {self.nextToken.value}') 


