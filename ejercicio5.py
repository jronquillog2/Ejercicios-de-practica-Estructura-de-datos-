import os
print("""*********************
Tabla de multiplicar
**********************""")
numero = int(input("Ingrese el numero del cual quiere ver la tabla de multiplicar: "))
for i in range(1, 11):
    resultado = i * numero
    print(numero, "x", i, "=", resultado)
os.system("pause")
