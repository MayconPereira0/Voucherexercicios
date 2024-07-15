class Conta:
    def __init__(self, nome, CPF, número, saldo):
        self.nome = nome
        self.CPF = CPF
        self.número = número
        self.saldo = saldo
    
    def imprimir_saldo(self):
        print(f'Saldo atual: R${self.saldo:.2f}')
    
    def deposito(self, valor_deposito):
        if valor_deposito > 0:
            self.saldo += valor_deposito
            print(f'Depósito de R${valor_deposito:.2f} realizado com sucesso.')
        else:
            print('Valor de depósito deve ser maior que zero.')

    def sacar(self, valor_sacar):
        if self.saldo >= valor_sacar:
            self.saldo -= valor_sacar
            print(f'Saque de R${valor_sacar:.2f} realizado com sucesso.')
        else:
            print('Saldo insuficiente')

nome = input("Digite o seu nome: ")
CPF = input("Digite o CPF: ")
número = int(input("Digite o número: "))
saldo = float(input("Digite o seu saldo: "))

dados = Conta(nome, CPF, número, saldo)

valor_deposito = float(input("Digite o valor que deseja depositar: "))
dados.deposito(valor_deposito)

valor_sacar = float(input("Digite o valor que deseja sacar: "))
dados.sacar(valor_sacar)

dados.imprimir_saldo()

  

        
    


