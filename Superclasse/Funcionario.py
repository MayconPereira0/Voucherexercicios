class Funcionario:
    def __init__(self,nome,matricula,salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario

    def bater_ponto(self,ponto):
        if ponto =='sim':
            print(f"{self.nome} já bateu o ponto!")
        elif ponto == 'não':
            print(f"{self.nome} ainda não bateu o ponto: ")

class Vendedor(Funcionario):
    def __init__(self,nome,matricula,salario,comissao,vendas):
        super().__init__(nome,matricula,salario)
        self.comissao = comissao
        self.vendas = vendas
    def bater_meta(self,meta):
        res = (self.comissao/100) * self.vendas
        if res >= meta:
            print("Meta batida!")
        else:
            print("Ainda não bateu a meta!")

class Gerente(Funcionario):
    def __init__(self,nome,matricula,salario,senha):
        super().__init__(nome,matricula,salario)
        self.senha = senha

    def login(self):
        if self.matricula and self.senha:
            print("Login realizado com sucesso!")
        else:
            print("Prescisa realizar o login!")
            