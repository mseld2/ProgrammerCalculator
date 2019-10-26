import unittest
from number import Number
from token_type import TokenType
from tokenizer import Tokenizer

class ToeknizerTests(unittest.TestCase):

    def test_can_tokenize_arithmetic_operators_with_mixed_positive_numbers(self):
        expr = '3 + xe5 - b101 * o16 // 8'
        tokenizer = Tokenizer(expr)
        tokens = tokenizer.tokenize()

        tokenList = []
        for token in tokens:
            tokenList.append(token)

        self.assertEqual(9, len(tokenList))
        self.assertEqual(TokenType.DECIMAL, tokenList[0].type)
        self.assertEqual('3', tokenList[0].value)
        self.assertEqual(TokenType.ADD, tokenList[1].type)
        self.assertEqual('+', tokenList[1].value)
        self.assertEqual(TokenType.HEX, tokenList[2].type)
        self.assertEqual('0xe5', tokenList[2].value)        
        self.assertEqual(TokenType.MINUS, tokenList[3].type)
        self.assertEqual('-', tokenList[3].value)
        self.assertEqual(TokenType.BINARY, tokenList[4].type)
        self.assertEqual('0b101', tokenList[4].value)
        self.assertEqual(TokenType.MULTIPLY, tokenList[5].type)
        self.assertEqual('*', tokenList[5].value)
        self.assertEqual(TokenType.OCTAL, tokenList[6].type)
        self.assertEqual('0o16', tokenList[6].value)        
        self.assertEqual(TokenType.DIVIDE, tokenList[7].type)
        self.assertEqual('//', tokenList[7].value)
        self.assertEqual(TokenType.DECIMAL, tokenList[8].type)
        self.assertEqual('8', tokenList[8].value)

    def test_can_tokenize_arithmetic_operators_with_mixed_negative_numbers(self):
        expr = '-3 + -xe5 - -b101 * -o16 // -8'
        tokenizer = Tokenizer(expr)
        tokens = tokenizer.tokenize()

        tokenList = []
        for token in tokens:
            tokenList.append(token)

        self.assertEqual(14, len(tokenList))
        self.assertEqual(TokenType.MINUS, tokenList[0].type)
        self.assertEqual('-', tokenList[0].value)
        self.assertEqual(TokenType.DECIMAL, tokenList[1].type)
        self.assertEqual('3', tokenList[1].value)
        self.assertEqual(TokenType.ADD, tokenList[2].type)
        self.assertEqual('+', tokenList[2].value)
        self.assertEqual(TokenType.MINUS, tokenList[3].type)
        self.assertEqual('-', tokenList[3].value)
        self.assertEqual(TokenType.HEX, tokenList[4].type)
        self.assertEqual('0xe5', tokenList[4].value)        
        self.assertEqual(TokenType.MINUS, tokenList[5].type)
        self.assertEqual('-', tokenList[5].value)
        self.assertEqual(TokenType.MINUS, tokenList[6].type)
        self.assertEqual('-', tokenList[6].value)       
        self.assertEqual(TokenType.BINARY, tokenList[7].type)
        self.assertEqual('0b101', tokenList[7].value)
        self.assertEqual(TokenType.MULTIPLY, tokenList[8].type)
        self.assertEqual('*', tokenList[8].value)
        self.assertEqual(TokenType.MINUS, tokenList[9].type)
        self.assertEqual('-', tokenList[9].value)        
        self.assertEqual(TokenType.OCTAL, tokenList[10].type)
        self.assertEqual('0o16', tokenList[10].value)        
        self.assertEqual(TokenType.DIVIDE, tokenList[11].type)
        self.assertEqual('//', tokenList[11].value)
        self.assertEqual(TokenType.MINUS, tokenList[12].type)
        self.assertEqual('-', tokenList[12].value)        
        self.assertEqual(TokenType.DECIMAL, tokenList[13].type)
        self.assertEqual('8', tokenList[13].value)

    def test_can_tokenize_group_lshift_or_operators(self):
        expr = '(b11010101 << 4) | x0F'

        tokenizer = Tokenizer(expr)
        tokens = tokenizer.tokenize()

        tokenList = []
        for token in tokens:
            tokenList.append(token)

        self.assertEqual(7, len(tokenList))
        self.assertEqual(TokenType.LPAREN, tokenList[0].type)
        self.assertEqual('(', tokenList[0].value)           
        self.assertEqual(TokenType.BINARY, tokenList[1].type)
        self.assertEqual('0b11010101', tokenList[1].value)            
        self.assertEqual(TokenType.LSHIFT, tokenList[2].type)
        self.assertEqual('<<', tokenList[2].value)  
        self.assertEqual(TokenType.DECIMAL, tokenList[3].type)
        self.assertEqual('4', tokenList[3].value)         
        self.assertEqual(TokenType.RPAREN, tokenList[4].type)
        self.assertEqual(')', tokenList[4].value)          
        self.assertEqual(TokenType.OR, tokenList[5].type)
        self.assertEqual('|', tokenList[5].value)          
        self.assertEqual(TokenType.HEX, tokenList[6].type)
        self.assertEqual('0x0F', tokenList[6].value)          

    def test_can_tokenize_group_rshift_and_operators(self):
        expr = '(b11010101 >> 4) & xF0'

        tokenizer = Tokenizer(expr)
        tokens = tokenizer.tokenize()

        tokenList = []
        for token in tokens:
            tokenList.append(token)

        self.assertEqual(7, len(tokenList))
        self.assertEqual(TokenType.LPAREN, tokenList[0].type)
        self.assertEqual('(', tokenList[0].value)           
        self.assertEqual(TokenType.BINARY, tokenList[1].type)
        self.assertEqual('0b11010101', tokenList[1].value)            
        self.assertEqual(TokenType.RSHIFT, tokenList[2].type)
        self.assertEqual('>>', tokenList[2].value)  
        self.assertEqual(TokenType.DECIMAL, tokenList[3].type)
        self.assertEqual('4', tokenList[3].value)         
        self.assertEqual(TokenType.RPAREN, tokenList[4].type)
        self.assertEqual(')', tokenList[4].value)          
        self.assertEqual(TokenType.AND, tokenList[5].type)
        self.assertEqual('&', tokenList[5].value)          
        self.assertEqual(TokenType.HEX, tokenList[6].type)
        self.assertEqual('0xF0', tokenList[6].value)  

    @unittest.expectedFailure
    def test_fails_when_unexpected_value_found(self):
        expr = '(13 % 8) w'                    

        tokenizer = Tokenizer(expr)
        tokenizer.tokenize()