def funA(n):
    return n * 100

def funC(n, f):
    return f(n) * 3

print(funC(9, funA))
