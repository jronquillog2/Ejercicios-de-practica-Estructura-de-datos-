import os
print("""*******************************
Division mostrando el cociente
*******************************""")
a = int(input("ingrese el primer valor: "))
b = int(input("ingrese el segundo  valor: "))
cociente=0
while a >= b:
    a = a - b
    cociente = cociente + 1
    break
print ("el cociente es: ", cociente)
print ("el resto es: ", a)

os.system("pause")



