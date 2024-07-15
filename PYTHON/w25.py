soma = 0
cont = 0

while True:
    idades = int(input("Digite as idades:"))
    if idades == 0:
        break
    soma += idades
    cont += 1

if cont > 0:
    media = soma / cont
    print("A média das idades é:", media)