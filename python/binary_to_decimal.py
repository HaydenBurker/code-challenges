# Create a function that takes a binary number and converts it to an integer

def binary_to_decimal(binary):
    decimal = 0
    for i, bit in enumerate(reversed(binary)):
        decimal += bit * 2 ** i
    return decimal

print(binary_to_decimal([0, 0, 0, 0, 0, 0, 0, 0])) # 0
print(binary_to_decimal([1, 1, 1, 1, 1, 1, 1, 1])) # 255
print(binary_to_decimal([1, 0, 1, 0, 1, 1, 0, 1])) # 173
print(binary_to_decimal([0, 1, 1, 0, 0, 1, 0, 0])) # 100