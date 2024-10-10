# Write a function that takes in a list and returns a nested list for each element in the list that is filled with that element and is the same length as the original list

def list_multiplier(l):
    return [[e] * len(l) for e in l]

print(list_multiplier(["Hello", "World"])) # [["Hello", "Helo"], ["World", "World"]]
print(list_multiplier([])) # []
print(list_multiplier([1])) # [[1]]
print(list_multiplier([1, 2, 3, 4, 5])) # [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]