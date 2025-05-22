# Write a function that takes the base and height of a triangle and returns the area. The base and height are non-negative whole numbers

def area_of_a_triangle(base, height):
    return base * height // 2


print(area_of_a_triangle(2, 3)) # 3
print(area_of_a_triangle(10, 10)) # 50
print(area_of_a_triangle(3, 4)) # 6
print(area_of_a_triangle(5, 0)) # 0