a = float(input("Digite o tamanho da área a ser pintada:"))
print("Situação 1")
quant = a/108
quanti = round(quant, 2)
custo = quant*80
custon = round(custo, 2)
print(f"será necessário {quanti} latas de 18L e custará {custon}R$")
print("Situação 2")
quant = a/28.8
quanti = round(quant, 2)
custo = quant*25
custon = round(custo, 2)
print(f"será necessário {quanti} galões de 3.6L e custará {custon}R$")