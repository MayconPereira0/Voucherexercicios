class Aluno:
    def __init__(self,nome,RA,n1,n2,n3,n4):
        self.nome = nome
        self.RA = RA
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4

    def mostrar_dados(self):
        print(f"{self.nome},{self.RA}")

    def soma_notas(self):
        (self.n1 + self.n2 + self.n3 + self.n4) / 4

nome = input("Digite o nome do aluno: ")
RA = int(input("Digite o RA do aluno: "))
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))

dados = Aluno(nome,RA,n1,n2,n3,n4)

dados

if soma >= 7:
    print(f"Aluno tirou {soma}, está APROVADO!")
elif soma < 7 or soma > 5.9:
    print(f"Aluno tirou {soma}, está de EXAME!")
else:
    print(f"Aluno tirou {soma}, está REPROVADO!")



