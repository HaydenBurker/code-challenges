# Write a function that takes the volume of a cube and returns the length of the diagonal rounded to three decimal places

def cube_diagonal(volume):
    return round(volume ** (1 / 3) * 3 ** (1 / 2), 3)

print(cube_diagonal(8)) # 3.464
print(cube_diagonal(100)) # 8.039
print(cube_diagonal(3.14)) # 2.536
print(cube_diagonal(216)) # 10.392