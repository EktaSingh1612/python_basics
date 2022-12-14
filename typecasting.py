a='2'
b='4'
print(a+b) #ans=12 since both are string

'''
TYPECASTING : The conversion of one data type into the other data type is known as type casting or type conversion.
Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.

2 types of typecasting:

1. Explicit conversion : the conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement.
It can be achieved with the help of python's built-in type conversion function such as int(), float(), hex(), oct(), str(), etc.
'''
string = '15'
number = 7
print(int(15)+7)

'''
2. Implicit conversion : data types in python do not have the same level i.e, ordereing of data types is not the same in python. Some of the data types have higher-order, and some have lower order. While performing any oprations on variables on variables with diff data types in python, one of the variable's data type is converted into other by the python interpretor itself (automatically). This is called implicit typecasting.

Python converts a smaller data type to a higher data type to prevent data loss.
'''

c=1.9
d=8
print(c+d)
print(type(c+d))