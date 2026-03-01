# Create a function that takes an integer and converts it to a binary number that is represented as a list of 0's and 1's

def decimal_to_binary(decimal):
    binary = []
    while True:
        binary.append(decimal % 2)
        decimal //= 2
        if decimal == 0:
            break
    zeros = [0] * max(0, 8 - len(binary))
    return zeros + list(reversed(binary))

print(decimal_to_binary(0)) # [0, 0, 0, 0, 0, 0, 0, 0]
print(decimal_to_binary(255)) # [1, 1, 1, 1, 1, 1, 1, 1]
print(decimal_to_binary(173)) # [1, 0, 1, 0, 1, 1, 0, 1]
print(decimal_to_binary(100)) # [0, 1, 1, 0, 0, 1, 0, 0]