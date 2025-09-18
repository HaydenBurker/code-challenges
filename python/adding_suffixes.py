# Write a function that returns a function that takes a string and adds a suffix to the end of it

def add_suffix(suffix):
    return lambda word: word + suffix

add_ful = add_suffix("ful")

print(add_ful("help")) # helpful
print(add_ful("fear")) # fearful
print(add_ful("grace")) # graceful

add_ing = add_suffix("ing")

print(add_ing("print")) # printing
print(add_ing("test")) # testing
print(add_ing("list")) # listing

add_ly = add_suffix("ly")

print(add_ly("miraculous")) # miraculously
print(add_ly(add_ful("grace"))) # gracefully
print(add_ly(add_ing("spar"))) # sparingly