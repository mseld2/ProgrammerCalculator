import unittest
from expr_parser import ExprParser

class ExprParseTests(unittest.TestCase):

    def test_can_evaluate_negative_number(self):
        expr = '-x10'

        result = ExprParser().parse(expr)

        self.assertEqual(-0x10, result.number)

    def test_can_add(self):
        expr = '(10 + -20) + 30'

        result = ExprParser().parse(expr)

        self.assertEqual(20, result.number)

    def test_can_subtract(self):
        expr = '(60 - 40) - -10'

        result = ExprParser().parse(expr)

        self.assertEqual(30, result.number)        

    def test_can_add_and_subtract(self):
        expr = '(-60 - 40) + 10'

        result = ExprParser().parse(expr)

        self.assertEqual(-90, result.number)  

    def test_can_multiply(self):
        expr = '(20 * -xA) * 5'

        result = ExprParser().parse(expr)

        self.assertEqual(-1000, result.number)       

    def test_can_divide(self):
        expr = '20 // -10'

        result = ExprParser().parse(expr)

        self.assertEqual(-2, result.number)    

    def test_can_multiply_and_divide(self):
        expr = '(-x14 // 10) * 5'

        result = ExprParser().parse(expr)

        self.assertEqual(-10, result.number)  

    def test_can_get_remainder(self):
        expr = '13 % 8'

        result = ExprParser().parse(expr)

        self.assertEqual(5, result.number)

    def test_can_lshift_and(self):
        expr = '(b00001111 << 4) & xF0'

        result = ExprParser().parse(expr)

        self.assertEqual(0xF0, result.number)   

    def test_can_rshift_or(self):
        expr = '(b11110000 >> 4) | x0F'

        result = ExprParser().parse(expr)

        self.assertEqual(0x0F, result.number)  

    def test_can_xor(self):
        expr = 'b11110000 ^ x0F'

        result = ExprParser().parse(expr)

        self.assertEqual(0xFF, result.number)  

    def test_can_invert(self):
        expr = '~xF0'

        result = ExprParser().parse(expr)

        self.assertEqual(-0xF0 - 1, result.number)                                   