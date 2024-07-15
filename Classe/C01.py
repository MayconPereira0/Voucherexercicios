class Pessoa:
    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_dados(self):
        print(f"Nome: {self.nome} - idade: {self.idade} - Rua: {self.endereco}")

    def altera_idade(self,nova_idade):
        self.idade = nova_idade
    
p = Pessoa("Maycon",18,"José")

p.mostrar_dados()

nova_idade = input("Digite a nova idade:")

p.altera_idade(nova_idade)

p.mostrar_dados()

