import os

mayor = 0
n = int (input ("cuantos valores desea ingresar: "))
print("****************")
for i in range (1, n + 1):
    un_numero = float (input ("Ingresa el valor de un numero: "))
    if i==1 or mayor<un_numero:
        mayor=un_numero

    print ()
print ("el mayor es: ",mayor)
os.system ("pause")



