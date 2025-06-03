"""Haz una función llamada area_triangulo que reciba la base y la altura y devuelva el área.
Fórmula: área = (base * altura) / 2"""

def area_triangulo (base,altura):
    return (base * altura) / 2

base = int(input("Ingresa la base del triangulo: "))
altura = int(input("Ingresa la altura del triangulo: "))

area = area_triangulo (base,altura)
print(f"EL area del triangulo es: ", area)