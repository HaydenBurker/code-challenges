# Create a function that takes in a string and returns a string showing all the missing letters that were not in the string
# All letters are lowercased ranging from a to z

import string

def get_missing_letters(letters):
    missing_letters = set(string.ascii_lowercase)
    for l in set(letters):
        if l in missing_letters:
            missing_letters.remove(l)
    return "".join(sorted(missing_letters))

print(get_missing_letters("abc")) # "defghijklmnopqrstuvwxyz"
print(get_missing_letters("helloworld")) # "abcfgijkmnpqstuvxyz"
print(get_missing_letters("abcdefghijklmnopqrstuvwxyz")) # ""
print(get_missing_letters("")) # abcdefghijklmnopqrstuvwxyz
print(get_missing_letters("snegkzmorpqgzknalprjgdsnvlxr")) # bcfhituwy