import os
print("""********************
Mayor de dos numeros
*********************""")
a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))
if a > b:
    mayor = a
else:
    mayor = b
print("El numero mayor es : ", mayor)
os.system("pause")