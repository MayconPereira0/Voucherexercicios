numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Inicializando variáveis para armazenar a soma dos números pares e a multiplicação dos números ímpares
soma_pares = 0
multiplicacao_impares = 1

# Inicializando o número atual como o menor número digitado
numero_atual = min(numero1, numero2)

# Enquanto o número atual estiver dentro do intervalo entre os números digitados
while numero_atual <= max(numero1, numero2):
    # Verificando se o número atual é par
    if numero_atual % 2 == 0:
        soma_pares += numero_atual
    # Verificando se o número atual é ímpar
    else:
        multiplicacao_impares *= numero_atual
    # Passando para o próximo número
    numero_atual += 1

# Exibindo os resultados
print("A soma dos números pares é:", soma_pares)
print("A multiplicação dos números ímpares é:", multiplicacao_impares)