# Create a function that takes in a num and splits the digits into an array of numbers

def num_split(num):
    return [int(n) * (1 if num >= 0 else -1) for n in list(str(abs(num)))]

print(num_split(123)) # [1, 2, 3]
print(num_split(-456)) # [-4, -5, -6]
print(num_split(5)) # [5]
print(num_split(0)) # [0]
print(num_split(-1)) # [-1]
print(num_split(9001)) # [9, 0, 0, 1]