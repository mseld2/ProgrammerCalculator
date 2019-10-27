from tokenizer import Tokenizer
from tokenizer import Token
from token_type import TokenType
from number import Number

class ExprParser(object):
    '''
    Parser for grammar specified in 'language_definition.txt'
    See: https://en.wikipedia.org/wiki/Recursive_descent_parser

    NOTE: Parenthesis are needed to enforce precedence
    '''

    def parse(self, expr):
        self.tokens = Tokenizer(expr).tokenize()
        self.currentToken = None
        self.nextToken = None
        self._nextToken()

        return self.startExpr()


    def _nextToken(self):
        self.currentToken, self.nextToken = self.nextToken, next(self.tokens, None)
        if self.currentToken:
            print(f'Current token: {self.currentToken.value}')
        if self.nextToken:
            print(f'Next token: {self.nextToken.value}')

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

    # start_expr 
    #   := xor_expr { '|' xor_expr }
    def startExpr(self):
        '''
        start_expr 
            := xor_expr { '|' xor_expr }
        '''

        result = self.xorExpr()
        if self._accept(TokenType.OR):
            if self.currentToken.type != TokenType.OR:
                raise SyntaxError(f'Expected |, got {self.currentToken.value}')
            return result | self.xorExpr()
        
        return result


    def xorExpr(self):
        '''
        xor_expr 
            := and_expr { '^' and_expr }
        '''

        result = self.andExpr()
        if self._accept(TokenType.XOR):
            if self.currentToken.type != TokenType.XOR:
                raise SyntaxError(f'Expected ^, got {self.currentToken.value}')
            return result ^ self.andExpr()
        
        return result


    def andExpr(self):
        '''
        and_expr 
            := shift_expr { '&' shift_expr }
        '''
        result = self.shiftExpr()
        if self._accept(TokenType.AND):
            if self.currentToken.type != TokenType.AND:
                raise SyntaxError(f'Expected &, got {self.currentToken.value}')
            return result & self.shiftExpr()
        
        return result

    def shiftExpr(self):
        '''
        shift_expr 
            := arith_expr { ( '<<' | '>>' ) arith_expr }
        '''

        result = self.arithExpr()
        if self._accept(TokenType.LSHIFT):
            if self.currentToken.type != TokenType.LSHIFT:
                raise SyntaxError(f'Expected <<, got {self.currentToken.value}')
            return result << self.arithExpr()
        elif self._accept(TokenType.RSHIFT):
            if self.currentToken.type != TokenType.RSHIFT:
                raise SyntaxError(f'Expected >>, got {self.currentToken.value}')
            return result >> self.arithExpr()
        
        return result

    def arithExpr(self):
        '''
        arith_expr
            := term { ( '+' | '-' ) term }
        '''

        result = self.term()
        if self._accept(TokenType.ADD):
            if self.currentToken.type != TokenType.ADD:
                raise SyntaxError(f'Expected +, got {self.currentToken.value}')           
            return result + self.term()
        elif self._accept(TokenType.MINUS):
            if self.currentToken.type != TokenType.MINUS:
                raise SyntaxError(f'Expected -, got {self.currentToken.value}')  
            return result - self.term()

        return result

    def term(self):
        '''
        term 
            := factor { ( '*' | '%' | '//' ) factor }
        '''
        result = self.factor()
        if self._accept(TokenType.MULTIPLY):
            if self.currentToken.type != TokenType.MULTIPLY:
                raise SyntaxError(f'Expected *, got {self.currentToken.value}')  
            return result * self.factor()
        elif self._accept(TokenType.REMAINDER):
            if self.currentToken.type != TokenType.REMAINDER:
                raise SyntaxError(f'Expected %, got {self.currentToken.value}')  
            return result % self.factor()
        elif self._accept(TokenType.DIVIDE):
            if self.currentToken.type != TokenType.DIVIDE:
                raise SyntaxError(f'Expected //, got {self.currentToken.value}')  
            return result // self.factor()
            
        return result

    def factor(self):
        '''
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
            raise SyntaxError(f'got unexpected token {self.nextToken.value}') 


