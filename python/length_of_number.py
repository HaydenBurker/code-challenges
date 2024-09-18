# Create a function that takes in a number and returns its length

def length_of_number(num):
    return len(str(num))

print(length_of_number(10)) # 2
print(length_of_number(0)) # 1
print(length_of_number(2000)) # 4
print(length_of_number(123456789)) # 9