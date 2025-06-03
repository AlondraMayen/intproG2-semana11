#Sumar dos números

def sumar (num1,num2): #Argumento (num1, num2)
    return num1 + num2

n1 = int(input("Ingresa un numero: ")) #Variable n1
n2 = int(input("Ingresa otro numero: "))
suma = sumar(n1, n2)
print(f"{n1} + {n2} = {suma}")