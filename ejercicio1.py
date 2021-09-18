import os
print("""***********************************************
Veamos si el numero que ingreso es par o impar
***********************************************""")
numero = int (input ("Ingresa un numero: "))
if numero%2==0:
    print ('El numero es par')
else:
    print ('El numero es impar')
print ()
os.system ("pause")