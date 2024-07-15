
def calcular_valor(consumo, preco):
    valor = consumo * preco
    return valor
def conta_energia(potencia, horas,  preco):
    consumo = potencia * horas / 1000
    conta = calcular_valor(consumo,preco)
    return conta

potencia = float(input("Digite a potência do aparelho: "))
tempo = float(input("Digite o tempo de uso do aparelho no mês: "))
preco = float(input("Digite o valor do kWh: "))

banho = conta_energia(potencia,tempo,preco)

print("R$: ",banho)