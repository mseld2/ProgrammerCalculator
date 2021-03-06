import re

class Number(object):
    '''
    A decimal (base 10), hex (base 16), binary (base 2) or octal (base 8) number
            Binary format: (-0b|0b)[0-1]+
            Hex format: (-0x|0x)[a-fA-F0-9]+
            Octal format: (-0o|0o)[0-7]+
            Decimal format: ([-]{0,1})[0-9]+
            
        Max (unsigned long long): 18,446,744,073,709,551,615
        Min (signed long long): -9,223,372,036,854,775,808
    '''

    def __init__(self):
        self._number = 0
        self._string = hex(0)

    def fromString(self, string):
        self._parse(string)

        return self

    def fromNumber(self, number):
        if number < self.min or number > self.max:
            raise ValueError(f'Number out of range: {number}')
        
        self._number = number
        self._setStringValues()

        return self

    @property
    def min(self):
        return -9_223_372_036_854_775_808

    @property
    def max(self):
        return 18_446_744_073_709_551_615

    @property
    def asHex(self):
        return self._asHex

    @property
    def asBinary(self):
        return self._asBinary

    @property
    def asOctal(self):
        return self._asOctal

    @property
    def asDecimal(self):
        return self._asDecimal

    @property
    def number(self):
        return self._number 

    def __invert__(self):       
        result = ~self._number

        return Number().fromNumber(result)

    def __add__(self, other):
        result = self.number + other.number

        return Number().fromNumber(result)

    def __sub__(self, other):
        result = self.number - other.number

        return Number().fromNumber(result)

    def __mul__(self, other):
        result = self.number * other.number

        return Number().fromNumber(result)

    def __floordiv__(self, other):
        result = self.number // other.number

        return Number().fromNumber(result)

    def __mod__(self, other):
        result = self.number % other.number

        return Number().fromNumber(result)

    def __lshift__(self, amount):
        if amount.number > 63 or amount.number < 0:
            raise IndexError(f'Shift amount out of range: {amount.asDecimal}')

        result = self.number << amount.number

        return Number().fromNumber(result)

    def __rshift__(self, amount):
        if amount.number > 63 or amount.number < 0:
            raise IndexError(f'Shift amount out of range: {amount.asDecimal}')

        result = self.number >> amount.number

        return Number().fromNumber(result)

    def __xor__(self, other):
        result = self.number ^ other.number

        return Number().fromNumber(result)

    def __and__(self, other):
        result = self.number & other.number

        return Number().fromNumber(result)

    def __or__(self, other):
        result = self.number | other.number

        return Number().fromNumber(result)  

    def _parse(self, string):
        if re.match("(-0b|0b)[0-1]+", string):
            self._number = int(string, 2)
        elif re.match("(-0x|0x)[a-fA-F0-9]+", string):
            self._number = int(string, 16)
        elif re.match("(-0o|0o)[0-7]+", string):
            self._number = int(string, 8)
        elif re.match("([-]{0,1})[0-9]+", string):
            self._number = int(string, 10)
        else:
            print("Invalid format\n")
            print("  Binary format: (-0b|0b)[0-1]+\n")
            print("  Hex format: (-0x|0x)[a-fA-F0-9]+\n")
            print("  Octal format: (-0o|0o)[0-7]+\n")
            print("  Decimal format: ([-]{0,1})[0-9]+\n")
            raise ValueError("Invalid format")

        if self.number < self.min or self.number > self.max:
            num = self._number
            self._number = 0
            raise ValueError(f'Number out of range: {num}')

        self._setStringValues()

    def _setStringValues(self):
        self._asBinary = self._group(bin(self.number))
        self._asHex = self._group(self.__str__())
        self._asOctal = self._group(oct(self.number))
        self._asDecimal = self._comma(str(self.number))

    def _group(self, value):
        '''
        Put binary, hex and octal digits in groups of 4
        0101 1001 0001 1000
        ffff 0000
        -0017
        '''
        start = 2
        if value[0] == '-':
            start = 3

        digits = value[start:]
        backwards = digits[::-1]
        str = ""
        for index in range(len(backwards)):
            if index > 0 and index % 4 == 0:
                str = f' {str}'
            str = f'{backwards[index]}{str}'

        fillers = 4 - (len(digits) % 4)
        if fillers != 4:
            for _ in range(fillers):
                str = f'{0}{str}'

        if start == 2:
            return f'{str}'
        else:
            return f'-{str}'

    def _comma(self, value):
        '''
        Add commas in decimal numbers
        -1,699
        100,000
        92
        '''
        start = 0
        if value[0] == '-':
            start = 1

        digits = value[start:]
        backwards = digits[::-1]

        str = ""
        for index in range(len(backwards)):
            if index > 0 and index % 3 == 0:
                str = f',{str}'
            str = f'{backwards[index]}{str}'

        if start == 0:
            return str
        else:
            return f'-{str}'

    def __str__(self):  
        string = hex(self._number)
        prefix = string[0:2]
        hexChars = string[2:]
        if string[0] == "-":
            prefix = string[0:3]
            hexChars = string[3:]
            
        return prefix.lower() + hexChars.upper()

    def __repr__(self):
        return self.__str__()


