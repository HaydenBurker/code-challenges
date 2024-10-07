# Create a function that takes a list of strings and returns the total number of uppercased characters found in the strings

def count_uppercase(string_list):
    return sum([len([c for c in s if c == c.upper() and c.isalpha()]) for s in string_list])

print(count_uppercase(["asdf", "JKL:"])) # 3
print(count_uppercase([])) # 0
print(count_uppercase(["Hello", "world!"])) # 1
print(count_uppercase(["The", "Quick", "Brown", "Fox", "Jumps", "Over", "The", "Lazy", "Dog"])) # 9