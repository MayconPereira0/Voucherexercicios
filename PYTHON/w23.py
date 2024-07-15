num = int(input("Digite um número:"))
soma = 0
for i in range(1,num):
    if num % i == 0:
        soma+= i
print("A soma dos divisores é:",soma)