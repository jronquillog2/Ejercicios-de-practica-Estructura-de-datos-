import os
print("""************************
Mayor y menor de n numeros
***************************""")

mayor = 0
menor = 0

n = int (input ("Ingresa el valor de n: "))
for i in range (1, n + 1):
    
    un_numero = float (input ("Ingresa el valor de un numero: "))
    if i==1 or un_numero<mayor:
        mayor=un_numero
    if i==1 or un_numero>menor:
        menor=un_numero

print ("Valor de mayor: ",mayor)
print ("Valor de menor: ",menor)

os.system ("pause")