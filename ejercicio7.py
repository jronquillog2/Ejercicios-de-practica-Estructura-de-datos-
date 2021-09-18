import os

print("""***********************************
Sumar hasta dar un numero negativo
***********************************""")
suma = 0
while True:
    numero = int(input("ingrese el numero: "))
    if numero < 0:
        print("*********Fin del proceso*********")
        break
    elif numero > 0:
        suma = suma + numero
        print("la suma es: ", suma)
os.system("pause")
