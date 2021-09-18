suma = 0
print("""****************
suma de 30 numeros primos
**************************""")

for i in range (1,31):
    print ("Numero" ,i)
    un_numero = int (input ("Ingresar numero primo: "))
    if un_numero%2==0:
        suma=suma+un_numero
    print ()
print ("Valor de suma: ", suma)