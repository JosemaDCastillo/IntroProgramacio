#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
def Nmax (n1, n2, n3):
    MAX = max(n1,n2,n3)
    print("El numero mayor es: ", MAX)

n1 = int(input("Dame un numero: "))
n2 = int(input("Dame un numero: "))
n3 = int(input("Dame un numero: "))
Nmax(n1, n2, n3)