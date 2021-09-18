import os
print("""***************************
Producto mediante una suma
***************************""")
a = int(input("ingrese el primer valor: "))
b = int(input("ingrese el segundo valor: "))
producto = int(0)
while b != 0:
    producto = producto + a
    b = b - 1
print("el producto entre los dos numeros es: ", producto)

os.system("pause")



