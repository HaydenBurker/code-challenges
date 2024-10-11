# Create a function that takes a list and returns the number of lists inside that list

def list_list_count(l):
    return len([o for o in l if type(o) == list])

print(list_list_count([[]])) # 1
print(list_list_count([1, 2, 3])) # 0
print(list_list_count([[1, 2, 3], ["Hello", "World"], [True, False], "Not a list"])) # 3
print(list_list_count([[1], [2], [3], [4], [5]])) # 5