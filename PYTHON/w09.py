numeros = []

for i in range(1, 11):
    numero = float(input(f"Digite o {i}º número: "))
    numeros.append(numero)

menor_valor = min(numeros)
maior_valor = max(numeros)

print("O menor valor lido é:", menor_valor)
print("O maior valor lido é:", maior_valor)