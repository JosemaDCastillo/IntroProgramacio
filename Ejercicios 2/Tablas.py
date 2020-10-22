#Tablas del 1 al 10

def tablaM():
    for s in range(1, 11):
        print("Tabla: ", s)
        for i in range(1, 11):
            print(s, " X ", i, " = ", i * s)

tablaM()