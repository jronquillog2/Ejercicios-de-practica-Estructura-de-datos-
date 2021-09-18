for i in (1,2):
    matriz=int(input("introduzca:[i ,j]: "))
for j in (2,2):
    matriz=int(input("introduzca:[i ,j]: "))
mayor=0
posicion_mayor_i=0
posicion_mayor_i=0
for i in range (2):
    for i in range (2):
        if matriz >mayor:
            mayor = matriz
            posicion_mayor_i=i
            posicion_mayor_j=j
print("El mayor es: ", mayor,"Su posicion es:",posicion_mayor_i,"-",posicion_mayor_j)
