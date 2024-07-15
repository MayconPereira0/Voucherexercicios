def calcular(peso):
    valor = 4.0
    if peso <= 50:
        print("Peso dentro da cota!")
        return peso
    else:
        peso_excesso = peso - 50
        paga_excesso = peso_excesso * valor
    return paga_excesso

peso = float(input("Digite o peso dos peixes:"))

valor_t = calcular(peso)

print(f"O peso excedido dará R${valor_t:.2f}")
