avaliacoes = int(input("Digite o número de avaliações do estudante: "))
soma_notas = 0
contador = 0
while contador<avaliacoes:
    nota = float(input(f"Digite a nota da avaliação {contador + 1}: "))
    soma_notas+=nota
    contador+=1

    media = soma_notas / avaliacoes

    print(media)


