print("""*********************
Suma de numeros pares
***********************""")
suma=0
n = int (input ("Ingresa el valor de n: "))
for i in range (1, n + 1):
    print ('Numero',i)
    un_numero = int (input ('Ingresa el valor de un numero: '))
    if un_numero%2==0:
        suma=suma+un_numero
    print ()
print ('Valor de suma de los numeros pare: ',suma)
