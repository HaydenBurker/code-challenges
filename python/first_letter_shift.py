# Create a function that shifts the first letters of each word to the next word
# Extra challenge: Make it so the capitalization of letters does not shift to the next word

def first_letter_shift(text):
    words = text.split(" ")
    temp = words[-1][0]
    first_is_calitalized = words[0][0].isupper()

    for i in reversed(range(len(words))):
        word = words[i]
        is_capitalized = word[0].isupper()
        first_letter = words[(i+len(words)-1)%len(words)][0]
        words[i] = f'{first_letter.upper() if is_capitalized else first_letter.lower()}{word[1:]}'


    words[0] = f'{temp.upper() if first_is_calitalized else temp.lower()}{words[0][1:]}'
    return " ".join(words)

print(first_letter_shift("hello world")) # "wello horld"
print(first_letter_shift("word")) # "word"
print(first_letter_shift("The quick brown fox jumps over the lazy dog")) # Dhe tuick qrown box fumps jver oth tazy log
print(first_letter_shift("This is a sentence. Here is another sentence.")) # Shis ts i aentence. Sere hs inother aentence.
print(first_letter_shift("Cycle until I am the original text")) # Tycle cntil U im ahe triginal oext
print(first_letter_shift(first_letter_shift(first_letter_shift(first_letter_shift(first_letter_shift(first_letter_shift(first_letter_shift("Cycle until I am the original text")))))))) # Cycle until I am the original text