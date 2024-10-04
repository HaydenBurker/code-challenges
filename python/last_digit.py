# Create a function that takes a list of numbers and returns a number where each digit of that number is the last digit of the list of numbers

def last_digits(nums):
    return sum([10 ** i * (n % 10) for (i, n) in enumerate(reversed(nums))])

print(last_digits([11, 22, 33, 44, 55])) # 12345
print(last_digits([7])) # 7
print(last_digits([12345, 543210])) # 50
print(last_digits([9, 8, 76, 543, 2, 1, 0])) # 9863210
print(last_digits([0, 0, 0])) # 0
print(last_digits([81936714])) # 4