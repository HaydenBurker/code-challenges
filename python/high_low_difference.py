# Create a function that takes in a non-negative whole number and retures the different between the largest and smallest number possible by rearranging the digits

def high_low_difference(number):
    return int("".join(sorted(list(str(number)), reverse=True))) - int("".join(sorted(list(str(number)))))

print(high_low_difference(54321)) # 41976
print(high_low_difference(66)) # 0
print(high_low_difference(0)) # 0
print(high_low_difference(1000000)) # 999999
print(high_low_difference(18496017)) # 97617321