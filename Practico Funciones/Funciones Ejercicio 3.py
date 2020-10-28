#Definir una función que calcule la longitud de una lista o una cadena dada.
def contador(lista):
    contador = 0
    for i in lista:
        contador = contador + 1
    return contador


palabra = input("Palabra: ")
numero = contador(palabra)
print(numero)