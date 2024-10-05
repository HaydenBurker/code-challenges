# Create a function that takes a list of numbers and returns a list of the sum of the numbers except for the one at the current index

def sum_of_other_numbers(nums):
    return [sum(nums[0:i] + nums[i+1: len(nums)]) for i in range(len(nums))]

print(sum_of_other_numbers([1, 2, 3])) # [5, 4, 3]
print(sum_of_other_numbers([10, -2, 5])) # [3, 15, 8]
print(sum_of_other_numbers([])) # []
print(sum_of_other_numbers([-1, -2, -3])) # [-5, -4, -3]
print(sum_of_other_numbers([5, -6, -3, 4])) # [-5, 6, 3, -4]