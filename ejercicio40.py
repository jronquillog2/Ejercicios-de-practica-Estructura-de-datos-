print("""**************************************
Buscar si se encuentra en el conjunto
**************************************""")
conjunto=set()

for i in range (1,6):
    print ('',i)
    un_conju = (input ("Ingrese aqui: "))
    conjunto.add(un_conju)
busc= input("ingrese lo que quiere saber si esta en el conjunto:")
print(busc in conjunto)
print(conjunto)