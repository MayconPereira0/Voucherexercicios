class Aluno_Academia:
    def __init__(self,Nome,idade,Peso,Altura,Mensalidade):
        self.Nome = Nome
        self.Idade = idade
        self.Peso = Peso
        self.Altura = Altura
        self.Mensalidade = Mensalidade ##120##

    def Calcular_IMC(self):
        calc = self.Peso / (self.Altura ** 2)
        print(f"Seu IMC é: {calc:.2f}")
    def Obter_valor_mansalidade(self):
        if self.Idade >= 18:
            des = 120.00
            print(f"Aluno maior de idade, mensalidade por: R${des}")
        else:
            desc = 100.00
            print(f"Aluno menor de idade, mensalidade por: R${desc}")
    
Nome = input("Digite seu nome: ")
Idade = int(input("Digite sua idade: "))
Peso = float(input("Digite seu peso: "))
Altura = float(input("Digite sua altura : "))
Mensalidade = 120.00

dados = Aluno_Academia(Nome,Idade,Peso,Altura,Mensalidade)

dados.Calcular_IMC()
dados.Obter_valor_mansalidade()


