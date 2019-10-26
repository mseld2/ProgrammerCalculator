import unittest
from number import Number

class NumberOpTests(unittest.TestCase):

    def test_can_add_with_positive_result(self):
        left = Number().fromNumber(0x17)
        right = Number().fromNumber(0x07)

        result = left + right

        self.assertEqual(0x1E, result.number)
        self.assertEqual("0x1E", result.asHex)

    def test_can_add_with_negative_result(self):
        left = Number().fromNumber(-0x17)
        right = Number().fromNumber(-0x07)

        result = left + right

        self.assertEqual(-0x1E, result.number)
        self.assertEqual("-0x1E", result.asHex)      

    @unittest.expectedFailure
    def test_fails_if_add_overflow(self):
        left = Number().fromNumber(18_446_744_073_709_551_615)
        right = Number().fromNumber(1)

        left + right    

    @unittest.expectedFailure
    def test_fails_if_add_underflow(self):
        left = Number().fromNumber(-1)
        right = Number().fromNumber(-9_223_372_036_854_775_808)

        left + right              

    def test_can_multiply_with_positive_result(self):
        left = Number().fromNumber(0x17)
        right = Number().fromNumber(0x07)

        result = left * right

        self.assertEqual(0xA1, result.number)
        self.assertEqual("0xA1", result.asHex)             

    def test_can_multiply_with_negative_result(self):
        left = Number().fromNumber(0x17)
        right = Number().fromNumber(-0x07)

        result = left * right

        self.assertEqual(-0xA1, result.number)
        self.assertEqual("-0xA1", result.asHex)      

    @unittest.expectedFailure
    def test_fails_if_multiply_overflow(self):
        left = Number().fromNumber(18_446_744_073_709_551_615)
        right = Number().fromNumber(2)

        left * right  

    @unittest.expectedFailure
    def test_fails_if_multiply_underflow(self):
        left = Number().fromNumber(-9_223_372_036_854_775_808)
        right = Number().fromNumber(2)

        left * right        

    def test_can_divide_with_positive_result(self):
        left = Number().fromNumber(0x10)
        right = Number().fromNumber(0x04)

        result = left // right

        self.assertEqual(0x04, result.number)
        self.assertEqual("0x4", result.asHex)                 

    def test_can_divide_with_negative_result(self):
        left = Number().fromNumber(-0x10)
        right = Number().fromNumber(0x04)

        result = left // right

        self.assertEqual(-0x04, result.number)
        self.assertEqual("-0x4", result.asHex)

    @unittest.expectedFailure
    def test_cannot_divide_by_0(self):
        left = Number().fromNumber(0x10)
        right = Number().fromNumber(0x00)

        left // right 

    def test_can_subtract_with_positive_result(self):
        left = Number().fromNumber(0x20)
        right = Number().fromNumber(0x10)

        result = left - right
      
        self.assertEqual(16, result.number)
        self.assertEqual("0x10", result.asHex) 

    def test_can_subtract_with_negative_result(self):
        left = Number().fromNumber(0x10)
        right = Number().fromNumber(0x20)

        result = left - right
      
        self.assertEqual(-16, result.number)
        self.assertEqual("-0x10", result.asHex)                                     

    @unittest.expectedFailure
    def test_fails_if_subtraction_overflow(self):
        left = Number().fromNumber(1)
        right = Number().fromNumber(-18_446_744_073_709_551_615)

        left - right          

    @unittest.expectedFailure
    def test_fails_if_subtraction_underflow(self):
        left = Number().fromNumber(-9_223_372_036_854_775_808)
        right = Number().fromNumber(1)

        left - right 

    def test_can_invert(self):
        value = Number().fromNumber(0x15)

        result = ~value

        self.assertEqual(-22, result.number)
        self.assertEqual("-0x16", result.asHex)

    def test_can_shift_left(self):
        value = Number().fromNumber(0b1101010) 

        result = value << 1

        self.assertEqual(0b11010100, result.number) 
        self.assertEqual("0b11010100", result.asBinary)

    @unittest.expectedFailure
    def test_fails_if_negative_shift_left(self):
        value = Number().fromNumber(0b1101010)

        value >> -1       

    @unittest.expectedFailure
    def test_fails_if_amount_too_large_left_shift(self):
        value = Number().fromNumber(0b1101010)  

        value >> 64                

    def test_can_shift_right(self):
        value = Number().fromNumber(0b11010100) 

        result = value >> 1

        self.assertEqual(0b1101010, result.number) 
        self.assertEqual("0b1101010", result.asBinary)

    @unittest.expectedFailure
    def test_fails_if_negative_shift_right(self):
        value = Number().fromNumber(0b11010100)  

        value >> -1       

    @unittest.expectedFailure
    def test_fails_if_amount_too_large_right_shift(self):
        value = Number().fromNumber(0b11010100)  

        value >> 64 

    def test_can_and(self):
        left = Number().fromNumber(0b110101) 
        right = Number().fromNumber(0b1)

        result = left & right

        self.assertEqual(0x01, result.number) 
        self.assertEqual("0b1", result.asBinary)

    def test_can_xor(self):
        left = Number().fromNumber(0b110101) 
        right = Number().fromNumber(0b11) 

        result = left ^ right

        self.assertEqual(0b110110, result.number) 
        self.assertEqual("0b110110", result.asBinary)    

    def test_can_or(self):
        left = Number().fromNumber(0b110101) 
        right = Number().fromNumber(0b11) 

        result = left | right

        self.assertEqual(0b110111, result.number) 
        self.assertEqual("0b110111", result.asBinary)