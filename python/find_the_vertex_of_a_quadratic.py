# Create a function that calculates the vertex coordinates of the quadratic equation ax^2 + bx + c given the values a, b, and c

def quadratic_vertex(a, b, c):
    x = -b/(2*a)
    y = a*x*x + b*x + c
    return (x, y)

print(quadratic_vertex(1, 0, 10)) # (0, 10)
print(quadratic_vertex(1, -2, -4)) # (1, -5)
print(quadratic_vertex(4, 4, 10)) # (-0.5, 9)
print(quadratic_vertex(-5, 20, 0)) # (2, 20)