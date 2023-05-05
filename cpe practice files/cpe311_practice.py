
b_num = list(input("input a binary number:"))
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


