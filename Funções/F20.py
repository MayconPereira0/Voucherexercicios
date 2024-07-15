import random

def sorteia_aluno(quant):
   alunos = []
   i = 0
   while i <= quant:
      nome = input("Digite o no nome do aluno: ")
      alunos.append(nome)
      i += 1

   escolhido = random.choice(alunos)
   print(f"O aluno escolhido foi: {escolhido}")

quant = int(input("Digite a quantidade de alunos que deseja sortear: "))
sorteia_aluno(quant)
