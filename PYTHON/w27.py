n1 = int(input("Digite um número:"))
cont = 1
for i in range(1, n1+1):
    cont *= i
print(cont)
    
n1 = int(input("Digite um número: "))  # Solicita ao usuário que digite um número
cont = 1  # Inicializa o contador com 1
resultado = 1  # Inicializa o resultado com 1

# Executa o loop enquanto o contador for menor ou igual ao número fornecido
while cont <= n1:
    resultado *= cont  # Multiplica o resultado pelo valor atual do contador
    cont += 1  # Incrementa o contador

# Imprime o resultado do fatorial
print(f"O fatorial de {n1} é {resultado}")