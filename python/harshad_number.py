# Create a function that determines of a number is a harshad number
# A harshad number is a number that is divisible by the sum of its digits

def harshad_number(num):
    digit_sum = sum((int(digit) for digit in str(num)), 0)
    return num % digit_sum == 0

print(harshad_number(111)) # True
print(harshad_number(6)) # True
print(harshad_number(35)) # False
print(harshad_number(5500)) # True
print(harshad_number(66)) # False