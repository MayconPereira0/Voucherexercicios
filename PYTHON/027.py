print("Escolha a opção:")
print("1- Soma de 2 números.")
print("2- Diferença entre 2 números (maior pelo menor).")
print("3- Produto entre 2 números.")
print("4- Divisão entre 2 números (o denominador não pode ser zero).")    

opcao = int(input("Digite o número da operação desejada:(1/2/3/4):"))

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if opcao == 1:
    res = n1 + n2
elif opcao == 2:
    res = abs(n1-n2)
elif opcao == 3:
    res = n1 * n2
elif opcao == 4:
    if n1 == 0:
        print ("Erro: denominador não pode ser zero")
    else:
        res = n1 / n2

else:
    res = "Opção inválida"

print("O resultado da operação é:", res)

