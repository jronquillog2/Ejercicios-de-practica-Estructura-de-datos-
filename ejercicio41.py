from typing import Counter


print("""**************************************
Leer cuantas palabras tiene un parrafo
**************************************""")
parrafo=input("ingrese el parrafo: ")
resultado=len(parrafo.split())
print("tiene",resultado,"palabras")

