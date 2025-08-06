# Write a recursive function that find the highest integer in a list
# Return None if the list is empty

def find_highest(l):
    if len(l) == 0:
        return None
    elif len(l) == 1:
        return l[0]
    return max(l[-1], find_highest(l[:-1]))

print(find_highest([2, 6, 4])) # 6
print(find_highest([-10, -3, -42, -11])) # -3
print(find_highest([])) # None
print(find_highest([100])) # 100
