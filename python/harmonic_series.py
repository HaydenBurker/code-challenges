# Create a function that calculates and returns 3 decimal places of the harmonic series (1/1 + 1/2 + 1/3 + ... + 1/(n-1) + 1/n) to the nth number

def harmonic_series(n):
    return float(f'{sum(1 / i for i in range(1, n+1)):.3f}')

print(harmonic_series(1)) # 1.0
print(harmonic_series(2)) # 1.5
print(harmonic_series(0)) # 0.0
print(harmonic_series(10)) # 2.929
print(harmonic_series(9000)) # 9.682