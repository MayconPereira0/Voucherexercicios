# Número de alunos e notas por aluno
num_alunos = 10
num_notas = 4

# Lista para armazenar as médias dos alunos
medias = []

# Loop para obter as notas de cada aluno
aluno = 0
while aluno < num_alunos:
    print(f"Aluno {aluno + 1}")
    soma_notas = 0  # Variável para somar as notas do aluno

    # Loop para obter as 4 notas de cada aluno
    nota = 0
    while nota < num_notas:
        nota_valor = float(input(f"Digite a nota {nota + 1}: "))
        soma_notas += nota_valor  # Adiciona a nota à soma
        nota += 1

    # Calcula a média do aluno
    media = soma_notas / num_notas
    medias.append(media)  # Armazena a média na lista de médias
    aluno += 1

# Conta quantos alunos têm média maior ou igual a 7.0
alunos_com_media_maior_ou_igual_a_sete = 0
for media in medias:
    if media >= 7.0:
        alunos_com_media_maior_ou_igual_a_sete += 1

# Imprime o número de alunos com média maior ou igual a 7.0
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_com_media_maior_ou_igual_a_sete}")