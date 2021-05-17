print(2 * 3)  # Basic Arithmetic: +, -, /, *
print(2 ** 3)  # Basic Arithmetic: +, -, /, *
print(10 % 3)  # Modulus Op. : returns remainder of 10/3
print(1 + 2 * 3)  # order of operations
print(10 / 3.0)  # int's and doubles

# Assign variable to number, convert to string and print with string.
my_num = 5
print(str(my_num) + "My favorite number")

# abs absolute value (get pozitif number)
my_num = -5
print(abs(my_num))

# number, power (2,2,2 = 8)
print(pow(2, 3))

# which number nis higher or use min for min number
print(max(4,6))

# round number
print(round(4.7))

from math import *

# ignore after the "." or instead of floor use ceil for alwasy up in this case get 7
print(floor(6.8))


num = 10
num += 100  # +=, -=, /=, *=
print(num)

++num
print(num)

# Math module has useful math methods
import math

print(pow(2, 3))
print(math.sqrt(144))
print(round(2.7))


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier
