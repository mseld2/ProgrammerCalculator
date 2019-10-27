import unittest
from number import Number

class NumberCtorTests(unittest.TestCase):

    def test_parse_binary_positve_number_string(self):
        string = "0b11010100011"
        obj = Number().fromString(string)

        self.assertEqual(0x6A3, obj.number)
        self.assertEqual("06A3", obj.asHex)
        self.assertEqual("1,699", obj.asDecimal)
        self.assertEqual("3243", obj.asOctal)
        self.assertEqual("0110 1010 0011", obj.asBinary)

    def test_parse_binary_negative_number_string(self):
        string = "-0b11010100011"
        obj = Number().fromString(string)

        self.assertEqual(-0x6A3, obj.number)
        self.assertEqual("-06A3", obj.asHex)
        self.assertEqual("-1,699", obj.asDecimal)
        self.assertEqual("-3243", obj.asOctal)
        self.assertEqual("-0110 1010 0011", obj.asBinary)

    def test_parse_hex_positve_number_string(self):
        string = "0x6A3"
        obj = Number().fromString(string)

        self.assertEqual(0x6A3, obj.number)
        self.assertEqual("06A3", obj.asHex)
        self.assertEqual("1,699", obj.asDecimal)
        self.assertEqual("3243", obj.asOctal)
        self.assertEqual("0110 1010 0011", obj.asBinary)                

    def test_parse_hex_negative_number_string(self):
        string = "-0x6A3"
        obj = Number().fromString(string)

        self.assertEqual(-0x6A3, obj.number)
        self.assertEqual("-06A3", obj.asHex)
        self.assertEqual("-1,699", obj.asDecimal)
        self.assertEqual("-3243", obj.asOctal)
        self.assertEqual("-0110 1010 0011", obj.asBinary)         

    def test_parse_octal_positve_number_string(self):
        string = "0o3243"
        obj = Number().fromString(string)

        self.assertEqual(0x6A3, obj.number)
        self.assertEqual("06A3", obj.asHex)
        self.assertEqual("1,699", obj.asDecimal)
        self.assertEqual("3243", obj.asOctal)
        self.assertEqual("0110 1010 0011", obj.asBinary)                 

    def test_parse_octal_negative_number_string(self):
        string = "-0o3243"
        obj = Number().fromString(string)

        self.assertEqual(-0x6A3, obj.number)
        self.assertEqual("-06A3", obj.asHex)
        self.assertEqual("-1,699", obj.asDecimal)
        self.assertEqual("-3243", obj.asOctal)
        self.assertEqual("-0110 1010 0011", obj.asBinary)          

    def test_parse_decimal_positve_number_string(self):
        string = "1699"
        obj = Number().fromString(string)

        self.assertEqual(0x6A3, obj.number)
        self.assertEqual("06A3", obj.asHex)
        self.assertEqual("1,699", obj.asDecimal)
        self.assertEqual("3243", obj.asOctal)
        self.assertEqual("0110 1010 0011", obj.asBinary)  

    def test_parse_decimal_negative_number_string(self):
        string = "-1699"
        obj = Number().fromString(string)

        self.assertEqual(-0x6A3, obj.number)
        self.assertEqual("-06A3", obj.asHex)
        self.assertEqual("-1,699", obj.asDecimal)
        self.assertEqual("-3243", obj.asOctal)
        self.assertEqual("-0110 1010 0011", obj.asBinary)  

    @unittest.expectedFailure
    def test_fails_if_number_string_overflow(self):
        Number().fromString("18446744073709551616")

    @unittest.expectedFailure
    def test_fails_if_number_string_underflow(self):
        Number().fromString("-9223372036854775809")               

    def test_parse_binary_positve_number(self):
        number = 0b11010100011
        obj = Number().fromNumber(number)

        self.assertEqual(number, obj.number)
        self.assertEqual("06A3", obj.asHex)
        self.assertEqual("1,699", obj.asDecimal)
        self.assertEqual("3243", obj.asOctal)
        self.assertEqual("0110 1010 0011", obj.asBinary)

    def test_parse_binary_negative_number(self):
        number = -0b11010100011
        obj = Number().fromNumber(number)

        self.assertEqual(number, obj.number)
        self.assertEqual("-06A3", obj.asHex)
        self.assertEqual("-1,699", obj.asDecimal)
        self.assertEqual("-3243", obj.asOctal)
        self.assertEqual("-0110 1010 0011", obj.asBinary)

    def test_parse_hex_positve_number(self):
        number = 0x6A3
        obj = Number().fromNumber(number)

        self.assertEqual(number, obj.number)
        self.assertEqual("06A3", obj.asHex)
        self.assertEqual("1,699", obj.asDecimal)
        self.assertEqual("3243", obj.asOctal)
        self.assertEqual("0110 1010 0011", obj.asBinary)                

    def test_parse_hex_negative_number(self):
        number = -0x6A3
        obj = Number().fromNumber(number)

        self.assertEqual(number, obj.number)
        self.assertEqual("-06A3", obj.asHex)
        self.assertEqual("-1,699", obj.asDecimal)
        self.assertEqual("-3243", obj.asOctal)
        self.assertEqual("-0110 1010 0011", obj.asBinary)          

    def test_parse_octal_positve_number(self):
        number = 0o3243
        obj = Number().fromNumber(number)

        self.assertEqual(number, obj.number)
        self.assertEqual("06A3", obj.asHex)
        self.assertEqual("1,699", obj.asDecimal)
        self.assertEqual("3243", obj.asOctal)
        self.assertEqual("0110 1010 0011", obj.asBinary)                 

    def test_parse_octal_negative_number(self):
        number = -0o3243
        obj = Number().fromNumber(number)

        self.assertEqual(number, obj.number)
        self.assertEqual("-06A3", obj.asHex)
        self.assertEqual("-1,699", obj.asDecimal)
        self.assertEqual("-3243", obj.asOctal)
        self.assertEqual("-0110 1010 0011", obj.asBinary)           

    def test_parse_decimal_positve_number(self):
        number = 1699
        obj = Number().fromNumber(number)

        self.assertEqual(number, obj.number)
        self.assertEqual("06A3", obj.asHex)
        self.assertEqual("1,699", obj.asDecimal)
        self.assertEqual("3243", obj.asOctal)
        self.assertEqual("0110 1010 0011", obj.asBinary)  

    def test_parse_decimal_negative_number(self):
        number = -1699
        obj = Number().fromNumber(number)

        self.assertEqual(number, obj.number)
        self.assertEqual("-06A3", obj.asHex)
        self.assertEqual("-1,699", obj.asDecimal)
        self.assertEqual("-3243", obj.asOctal)
        self.assertEqual("-0110 1010 0011", obj.asBinary)          

    @unittest.expectedFailure
    def test_fails_if_number_overflow(self):
        Number().fromNumber(18_446_744_073_709_551_616)

    @unittest.expectedFailure
    def test_fails_if_number_underflow(self):
        Number().fromNumber(-9_223_372_036_854_775_809)