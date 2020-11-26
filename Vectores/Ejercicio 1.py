def fact ():
    num = int(input("Factorial para: "))
    factorial = []

    for i in range(1,21):
        a = str(i) + "!"
        factorial.append(a)
    print(factorial)

    num2 = 1
    while num > 1:
        num2 = num * num2
        num = num-1
        print("El factorial de ", num, " es: ", num2)

fact ()