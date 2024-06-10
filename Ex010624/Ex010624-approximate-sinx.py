def factorial (x):
    result = 1
    for i in range (1, x+1):
        result = result * i
    return result

def approx_sin(x, n):
    sin = 0
    for i in range(n+1):
        sin = (-1)**i * (x**(2*i+1)/factorial(2*i+1))
        sin += sin
    return sin

print(approx_sin(1, 10))