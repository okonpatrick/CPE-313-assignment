'''b_num = list(input("input a binary number:"))
value = 0
for i in range(len(b_num)):
    digit = b_num.pop()
    if digit == '1':
        value = value + pow(2, i)
print('t1he decimal value of the number is', value)


# alternatively

bitString = input("Enter a string of bits: ")
decimal = 0
exponent = len(bitString) - 1
for digit in bitString:
    decimal = decimal + int(digit) * 2 ** exponent
    exponent = exponent - 1
print("The integer value is", decimal)


# decimal to binary program.

decimal = int(input("enter a decimal integer:"))
if decimal == 0:
    print(0)
else:
    print("Quotient Remainder Binary")
    bitString = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal//2
        bitString = str(remainder) + bitString
        print("%5d%8d%12s" % (decimal, remainder, bitString))
print("The binary representation is ", bitString)
'''
import random

s = "what is your name"

print(s.split())
print(s.find("a"))
print(s.endswith("f"))
print(s.startswith("W")) #fale because of capital letter
print(s.isalpha())
print(s.replace("name", "problem"))
print(random.randrange(1, 10))

print("How to manipulate lists in python!")
a = [8, 3.65, 'python', 90]
print(a[3])
print(a[2])
print(a[-3])
print(a[-2])


#not cpe 311 practice

for i in range(10):
    pass

def simpleFunction():
    "This is a cool simple function that returns 1"
    return 1
print(simpleFunction.__doc__[10:14])

import re

sum = 0

pattern = 'back'
if re.match(pattern, 'backup.txt'):
    sum += 1
if re.match(pattern, 'text.back'):
    sum += 2
if re.search(pattern, 'backup.txt'):
    sum += 4
if re.search(pattern, 'text.back'):
    sum += 8

print(type(sum))


class NumFactory:
    def __init__(self, n):
        self.val = n

    def timesTwo(self):
        self.val *= 2

    def plusTwo(self):
        self.val += 2


f = NumFactory(2)
for m in dir(f):
    mthd = getattr(f, m)
    if callable(mthd):
        mthd()

print(f.val)