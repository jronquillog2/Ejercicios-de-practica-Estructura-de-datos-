print("""*******************************
palabra mas larga del parrafo
******************************""")
parra =input("ingrese el parrafo: ")
re=max(parra.split(), key=len)
print("la palabra mas larga es:",re)



