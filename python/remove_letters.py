# Create a function that takes a list of letters and a string. The function should remove letters from the list that occur in the string and return the updated list

def remove_letters(l, s):
    for letter in s:
        for i in range(len(l)):
            if l[i] == letter:
                del l[i]
                break
    return l

print(remove_letters(['a', 'b', 'c', 'd', 'e', 'f'], "abc")) # ['d', 'e', 'f']
print(remove_letters(['e', 'm', 'p', 't', 'y'], "empty")) # []
print(remove_letters(['h', 'e', 'l', 'l', 'o'], "world")) # ['h', 'e', 'l']
print(remove_letters(['a', 'b', 'c'], "")) # ['a', 'b', 'c']
print(remove_letters([], "Nothing to remove")) # []