def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_euclidean(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

a = 32321
b = 26513
gcd, x, y = extended_euclidean(a, b)

print(f"gcd({a}, {b}) = {gcd}")
print(f"Coeficientes de Bézout: x = {x}, y = {y}")
print(f"Verificação: {a}*({x}) + {b}*({y}) = {a*x + b*y}")

