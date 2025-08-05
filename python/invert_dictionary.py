# Write a function that takes a dictionary and inverts the keys and values

def invert_dictionary(dict):
    return {value: key for (key, value) in dict.items()}

print(invert_dictionary({"a": 1, "b": 2, "c": 3})) # {1: "a", 2: "b", 3: "c"}
print(invert_dictionary({"Hello": "world!"})) # {"world!": "Hello"}
print(invert_dictionary({})) # {}