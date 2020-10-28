#Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
def caracteres(nCaracter, caracter):
    carac = (caracter*nCaracter)
    print(carac)

caracter = input("Dame el caracter para repetir: ")
num = int(input("Numeros de veces que quieres que se repita: "))
caracteres(num, caracter)