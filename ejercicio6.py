import os
print("""******************************
suma y producto de 30 numeros
******************************""")
sumatoria = 0
producto = 1
for i in range(1, 31):
    print(i)
    sumatoria = sumatoria+i
    producto = producto*i
print ("Valor de la sumatoria: ", sumatoria)
print ("Valor de producto: ", producto)
os.system("pause")
