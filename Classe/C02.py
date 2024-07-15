class Livro:
    def __init__(self,nome,autor,editora,paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def mostrar_dados(self):
        print(f"\n Nome do livro: {self.nome} \nAutor: {self.autor} \nEditora: {self.editora} \nQuant. Páginas: {self.paginas}")

    def alterar_editora(self, nova_editora):
        self.editora = nova_editora

    def alterar_pag(self, altera_pag):
        self.paginas = altera_pag

nova_editora = input("Digite a nova editora: ")
altera_pag = input("Digite a nova quantidade de páginas: ")

dados = Livro("Maycon","Maycon","Saraiva",100)

dados.alterar_pag(altera_pag)
dados.alterar_editora(nova_editora)

dados.mostrar_dados()



