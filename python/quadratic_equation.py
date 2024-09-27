# Create a function that returns the root values of x in any quadratic equation

def quadratic_equation(a, b, c):
    result = ((b*b - 4*a*c)**.5)
    return ((-b + result) / (2*a), (-b - result) / (2*a))


print(quadratic_equation(4, -9, 2)) # (-2, 0.25)
print(quadratic_equation(2, 1, -3)) # (1, -1.5)
print(quadratic_equation(1, -11, -26)) # (13, -2)