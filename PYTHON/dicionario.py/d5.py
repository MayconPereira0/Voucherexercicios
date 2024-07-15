
frase = input("Digite a frase ou texto:")

palavras = frase.split()

frequencia = {}

for palavra in palavras:
    frequencia[palavra] = frequencia.get(palavra, 0) + 1
print(frequencia)
