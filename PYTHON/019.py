n1 = int(input("Digite um número:"))

soma_digitos = 0

numero_str = str(n1)

for caractere in numero_str:
    soma_digitos += int(caractere)

print("A soma dos algorismos do número:",n1, "é:", soma_digitos)    

