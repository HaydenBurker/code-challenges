# Write a function that takes in a positive whole number and return true if a number is pandigital (contains all digits 0-9) and false otherwise

import string

def is_pandigital(num):
    return "".join(sorted(set(c for c in str(num)))) == string.digits

print(is_pandigital(1234567890)) # True
print(is_pandigital(98765433210)) # True
print(is_pandigital(1)) # False
print(is_pandigital(138045673926)) # True
print(is_pandigital(38423587049)) # False
print(is_pandigital(314159265358979)) # False
print(is_pandigital(1029384756)) # True