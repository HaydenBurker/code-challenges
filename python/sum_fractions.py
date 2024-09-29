# Create a function that takes in a list of fractions in the form [numerator, denominator] and returns the sum of them rounded to the nearest whole number

def sum_fractions(fractions):
    return round(sum([n / d for [n, d] in fractions]))

print(sum_fractions([[6, 3], [2, 3]])) # 3
print(sum_fractions([[7, 4], [20, 8]])) # 4
print(sum_fractions([[5, 2], [9, 3], [9, 10], [6, 15]])) # 7