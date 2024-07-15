def calc():
    preco = 1.99
    print("Loja quase 2 - Tabela de preços")
    for i in range (1,51):
        total = i * preco
        print(f"quantidade:{i} - R${total:.2f}")
calc()