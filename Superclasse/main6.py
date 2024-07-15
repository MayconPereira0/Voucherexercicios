from Funcionario import Funcionario
from Funcionario import Vendedor
from Funcionario import Gerente

while True:
    menu = int(input("Digite 1 para entar como vendedor física ou 2 para gerente: "))
    if menu == 1:
        nome = input("Digite o nome do vendedor: ")
        matri = input("Digite sua matrícula: ")
        ponto = input("Voçê já bateu o ponto:(sim/não)")
        salario = input("Digite seu salário: ")
        comissao = float(input("Digite sua comissaõ em %: "))
        vendas = float(input("Digite quanto fez em vendas: "))

        info = Vendedor(nome,matri,salario,comissao,vendas)
        info.bater_ponto(ponto)
        meta = float(input("Digite sua meta: "))
        info.bater_meta(meta)
    elif menu == 2:
        nome = input("Digite seu nome: ")
        matri = input("Digite sua matrícula: ")
        senha = input("Digite sua senha: ")
        salario = input("Digite seu salário: ")
        info2 = Gerente(nome,matri,senha,salario)

        info2.login()