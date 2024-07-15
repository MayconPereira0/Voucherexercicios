print("BOA TARDE!!!")

nome = input("Digite seu nome: ")
mes = input("Digite o mês de vencimento da fatura: ")
dia = input("Digite o dia de vencimento: ")
valor = float(input("Digite o valor da fatura: "))
valor = f"{valor:.2f}"

print(f"Olá {nome}")
print(f"A sua fatura com vencimento em {dia } de {mes} no valor de R$ {valor} está fechada.")