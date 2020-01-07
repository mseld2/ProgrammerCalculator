# Programmer Calculator

Simple calculator for programmers. 

Supported bases:
*  Decimal (base 10)
*  Hex (base 16)
*  Binary (base 2)
*  Octal (base 8)

Operations:
*  Shift
*  Invert (-x - 1)
*  Bitwise xor, and, or
*  Addition, subtraction
*  Multiplication, division, modulus

## Usage

```
> python calculater.py "<expression>"
```
  
```
> python calculator.py x12039    
    73,785   
0x  0001 2039   
0b  0001 0010 0000 0011 1001  
0o  0022 0071  
```

```
> python calculator.py "(b11110000 >> 4) & x0f"    
    15  
0x  0000F   
0b  1111  
0o  0017  
```

