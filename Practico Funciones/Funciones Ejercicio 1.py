#Definir una función que tome como argumento dos números y devuelva el mayor de ellos.

def max(num1,num2):
    if n1 > n2:
        print(n1, "es mayor que ", n2)
    else:
        print(n2, "es mayor que ", n1)

n1 = int(input("Dame un numero: "))
n2 = int(input("Dame otro numero: "))
max(n1,n2)