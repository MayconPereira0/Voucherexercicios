contador = 0
lista = []
while contador <= 10:
    cidades = input("Digite a cidade:")
    lista.append(cidades)
    contador += 1
for cidades in lista:
    print(cidades)

