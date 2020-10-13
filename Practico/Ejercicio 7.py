num = int(input("Numero: "))
divisor = 0
for divisor in range(1, num+1):
    if num % divisor == 0:
        print(divisor)