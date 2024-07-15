cont = 0
consoantes = []

p = input("Digite a palavra:")

i = 0
while i < len(p):
    caractere = p[i]
    if caractere.lower() >= 'a' and caractere.lower() <= 'z' and caractere.lower() not in 'aeiou':
        cont += 1
        consoantes.append(caractere)
    i += 1
print(f"Quantidade de consoantes lidas: {cont}")
print("Consoantes lidas:", consoantes)