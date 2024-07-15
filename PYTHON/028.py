idade = int(input("Digite sua idade:"))
tempo = float(input("Digite em anos o tempo trabalhado:"))

if idade >= 65:
    print("pode de aposentar")
elif tempo >= 30:
    print("pode de aposentar")
elif tempo >= 25 and idade >= 60:
    print("pode de aposentar")
else:
    print("Não pode de aposentar")



