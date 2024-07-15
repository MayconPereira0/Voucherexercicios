def inverso(num):
    num_str = str(num)           # Converte o número para uma string
    num_list = list(num_str)     # Converte a string em uma lista de caracteres
    num_list.reverse()           # Inverte a lista
    num_reverso_str = "".join(num_list)  # Junta os caracteres da lista de volta em uma string
    num_reverso = int(num_reverso_str)   # Converte a string resultante de volta para um número inteiro
    print(f"Número invertido é: {num_reverso}")

x = int(input("Digite o número: "))
inverso(x)