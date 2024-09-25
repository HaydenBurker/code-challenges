# Create a function that takes in a number and a length and returns a list containing multiples of the number until the length of the list reaches length

def list_of_multiples(num, length):
    return [num * i for i, num in enumerate([num] * length, 1)]

print(list_of_multiples(5, 7)) # [5, 10, 15, 20, 25, 30, 35]
print(list_of_multiples(24, 5)) # [24, 48, 72, 96, 120]
print(list_of_multiples(111, 9)) # [111, 222, 333, 444, 555, 666, 777, 888, 999]
print(list_of_multiples(5, 1)) # [5]
print(list_of_multiples(10, 0)) # []