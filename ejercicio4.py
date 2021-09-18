import os
print("""*********************
Mayor de tres numeros
**********************""")
a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))
c = float(input("Ingresa el tercer numero: "))
mayor = a
if mayor < b:
    mayor = b
if mayor < c:
    mayor = c
print("El numero mayor es: ", mayor)
os.system("pause")
