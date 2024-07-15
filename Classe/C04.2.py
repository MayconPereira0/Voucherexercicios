class Banco:
    def __init__(self,nome,sobrenome,horas_trabalhadas,valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def nomecompleto(self):
        print(f"Olá {self.nome} {self.sobrenome}")
    
    def calcula_s(self):
        s = self.horas_trabalhadas * self.valor_hora
        print(f"O seu sálario mensal é de: R${s:.2f}")
    
nome = input("Digite o seu nome: ")
sobrenome = input("Digite o sobrenome: ")
horas_trabalhadas = int(input("Digite as horas trabalhadas: "))
valor_hora = float(input("Digite o valor hora: "))


dados = Banco(nome,sobrenome,horas_trabalhadas,valor_hora)

dados.nomecompleto()
dados.calcula_s()
