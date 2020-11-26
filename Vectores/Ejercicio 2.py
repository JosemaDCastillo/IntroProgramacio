vectorA = []
vectorB = []
vectorSuma = []
suma1 = 0
suma2 = 0

for i in range (1, 6):
    i = str(i)
    num=int(input(f"Primer vector Nº{i}: "))
    vectorA.append(num)
    suma1 = suma1 + num

print("-")

for k in range (1, 6):
    k = str(k)
    num2=int(input(f"Segundo vector Nº{k}: "))
    vectorB.append(num2)
    suma2 = suma2 + num2

res = suma1 + suma2
print("Resultado= ", res)
for w in range (0, 5):
    suma = vectorA[w] + vectorB[w]
    vectorSuma.append(suma)

print(vectorA)
print(vectorB)
print(vectorSuma)