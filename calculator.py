import sys
from number import Number
from expr_parser import ExprParser

if len(sys.argv) != 2:
    raise RuntimeError(f'Expected 1 argumements, got {len(sys.argv) - 1}')

convert = False

result = ExprParser().parse(sys.argv[1])
print(f'    {result.asDecimal}')
print(f'0x  {result.asHex}')
print(f'0b  {result.asBinary}')
print(f'0o  {result.asOctal}')


