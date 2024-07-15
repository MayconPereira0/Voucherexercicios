base = int(input("Digite a base:"))
expoente = int(input("Digite o expoente:"))

res = 1
cont = 0

while cont <= base:
    res *= expoente
    cont += 1

print(f"{base}^{expoente} =", res)