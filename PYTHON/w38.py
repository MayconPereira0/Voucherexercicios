n = int(input('Digite um número inteiro positivo: '))
soma = 0
num = 2

while num <= n:
    primo = True
    i = 2
    while i < num:
        if num % i == 0:
            primo = False
            break
        i += 1
    if primo:
        print(num)
        soma += num
    num += 1

print(f"A soma dos números primos até {n} é: {soma}")