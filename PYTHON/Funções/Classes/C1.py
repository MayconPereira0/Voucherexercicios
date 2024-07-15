class Pessoa:
    nome = None
    idade = None
    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    def mostrar_dados(self):
        return self.nome, self.idade, self.endereco


pessoa = Pessoa("m",18,"j")
print(pessoa.mostrar_dados())


    

