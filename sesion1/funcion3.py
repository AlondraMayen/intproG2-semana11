""" Fórmula area = pi * (r * r)"""
def area (pi, r):
    return pi * (r * r)

pi = 3.14
r = float(input("Ingrese el radio: " ))
area = pi * (r * r)

print(f"El radio es: {pi} * ({r} * {r}) = {area} ")