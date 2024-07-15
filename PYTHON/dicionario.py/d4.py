items = {
    "Café":20,
    "Leite":10,
    "Ovos":30
}

compra = input("Digite o produto que deseja:")

if compra in items:
    print("O produto",compra, "está com",items[compra],"items no estoque!")
else:
    print("Produto indisponível!")