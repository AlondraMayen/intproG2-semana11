"""Escribe una función promedio que reciba tres notas y devuelva el promedio. 
Luego imprime si está aprobado (mayor o igual a 3) o reprobado."""

def promedio(num1, num2, num3):
    return (num1 + num2 + num3) / 3

nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

promediar = promedio(nota1, nota2, nota3)
print(f"El promedio es: {promediar:.2f}")

if promediar >= 3:
    print("Está aprobado.")
else:
    print("Está reprobado.")