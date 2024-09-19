# Create a function that shifts the first letters of each word to the next word

def first_letter_shift(sentence):
    words = sentence.split(" ")
    temp = words[0][0]
    for i, word in enumerate(words):
        words[i] = f'{words[(i+1)%len(words)][0]}{word[1:]}'

    words[-1] = f'{temp}{words[0][1:]}'
    return " ".join(words)

print(first_letter_shift("hello world")) # "wello horld"
print(first_letter_shift("word")) # "word"
print(first_letter_shift("the quick brown fox jumps over the lazy dog")) # qhe buick frown jox oumps tver lth dazy tog