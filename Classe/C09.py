class Carro:
    def __init__(self,Modelo,Marca,Cor,Ano,Valor,Nivel,Consumo):
        self.Modelo = Modelo
        self.Marca = Marca
        self.Cor = Cor
        self.Ano = Ano
        self.Valor = Valor
        self.Nivel = Nivel
        self.Consumo = Consumo

    def abastecer(self,abastece):
        self.Nivel += abastece
        print(f"Abastecimento de {abastece} litros realizado com successo. \nNivel de combustivel atual: {self.Nivel} l")

    def andar(self,Km):
        combustivel_gasto = Km / self.Consumo
        if combustivel_gasto <= self.Nivel:
            self.Nivel -= combustivel_gasto
            print(f"O carro andou {Km} km.")
        else:
            print("Combustível insuficiente para percorrer essa distância.")
        print(f"Nível de combustível atual: {self.Nivel}")

    def calcular_imposto(self):
        ipva = self.Valor * (2.5 / 100)
        print(ipva)

modelo = input("Digite o modelo do veículo: ")
marca = input("Digite a marca do veículo: ")
cor = input("Digite a cor do veículo: ")
ano = input("Digite o ano do veículo: ")
valor = float(input("Digite o valor do veículo: "))
nivel = float(input("Digite o nível de combustível do veículo: "))
consumo = float(input("Digite o consumo por Km do veículo: "))

dados = Carro(modelo,marca,cor,ano,valor,nivel,consumo)

abastece = float(input("Digite a quantidade de combustível que deseja: "))
dados.abastecer(abastece)

distancia = float(input("Digite quantos Km o carro percorreu: "))
dados.andar(distancia)

dados.calcular_imposto()
