num1 = int(input("Numero: "))
num2 = int(input("Segundo Numero: "))
num3 = int(input("Tercer Numero: "))
min = min(num1, num2, num3)
max = max(num1, num2, num3)
mid = (num1 + num2 + num3) - min -max
print(min, "  ", mid, "  ", max)
if min == max and max == mid:
    print("Los numeros son iguales")
