p1 = input("Ingrese una Palabra: ")
p2 = input("Ingrese una Degunda Palabra: ")
long_1 =len(p1)
long_2 =len(p2)
if long_1 > long_2:
    print(f"{p1} tiene {long_1 - long_2} letras mas que {p2}")
elif long_1 == long_2:
    print(f"{p1} tienen la misma de letras que {p2}")
else:
    print(f"{p2} tiene {long_2 - long_1} letras mas que {p1}")