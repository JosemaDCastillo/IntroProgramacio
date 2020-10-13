n1 = int(input("Primer Numero: "))
n2 = int(input("Segundo Numero: "))
suma = 0
for i in range (n1+1, n2):
    print(i)
    suma = suma + i
print("la suma es: ", suma)