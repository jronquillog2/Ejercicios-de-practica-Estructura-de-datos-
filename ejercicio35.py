print("""*******************************
CONVERSOR DE DECIMAL A BI-OC-HEX
*********************************""")
num=int(input("introduzca el numero que desea convertir: "))
print("""
1. Binario
2. Octal
3. Hexadecimal
""")
opc=(int(input("elija la opcion: ")))
if opc == 1:
    binario =bin(num) 
    print("su conversion es:", binario)
elif opc == 2:
    octal =oct(num) 
    print("su conversion es:", octal)
elif opc == 3:
    hexa=hex(num) 
    print("su conversion es:", hexa)
else:
    print("!!!!!esta opccion no existe!!!!!!")
