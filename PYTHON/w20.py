i = 0
i2 = 0

while True:
    num=int(input("Digite uma quantidade de números:"))
    if num == 0:
        break
    i += 1
    i2 += num % 2 == 0
print("Total de dados lidos:",i)
print("Total de números pares:",i2)