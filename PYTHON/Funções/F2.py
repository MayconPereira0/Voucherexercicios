def exp(base,expoente):
    exp = base ** expoente
    return exp

base = int(input("Digite a base:"))
expoente = int(input("Digite o expoente:"))

x = exp(base,expoente)

print("O expoente é:",x)
