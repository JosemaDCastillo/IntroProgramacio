#Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
def palindromo(palabra):
    tam = len(palabra)
    tam = tam - 1
    palabraInvertida = ""
    for indice in range(tam,-1,-1):
        palabraInvertida = palabraInvertida + palabra[indice]

    if palabraInvertida == palabra:
        print(palabra, " = True")
    else:
        print(palabra, " = False")

palabra = input("Dame una frase: ")
palindromo(palabra)