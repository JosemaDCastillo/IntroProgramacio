dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
cociente = dividendo // divisor
resto = dividendo % divisor
if dividendo % divisor == 0:
    print("La division es exacta")
else:
    print("La division no es exacta")
print("El cociente es: ", cociente)
print("El resto es: ", resto)