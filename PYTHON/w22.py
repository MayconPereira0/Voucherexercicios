soma = 0
cont_notas = 0

while True:
    nota = float(input("Digite uma nota: "))
    if nota < 0:
        break
    if nota > 10:
        break
    soma += nota
    cont_notas += 1

if cont_notas > 0:
    media = soma / cont_notas
    print("A média das notas é:", media)
