def adicao(a,b):
    return a + b
def subitracao(a,b):
    return a - b
def mutiplicacao(a,b):
    return a * b
def divisao(a,b):
    if b == 0:
        return "Erro: divisão por zero"
    else:
        return a / b
    
print("Escolha a operação matemática:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")    

opcao = int(input("Digite o número da operação desejada (1/2/3/4): "))

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if opcao == 1:
    res = adicao (valor1,valor2)
elif opcao == 2:
    res = subitracao (valor1,valor2)
elif opcao == 3:
    res = mutiplicacao (valor1,valor2)
elif opcao == 4:
    res = divisao (valor1,valor2)
else:
    res = "Opção inválida"

print("O resultado da operação é:", res)


