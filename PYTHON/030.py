

valor = float(input("Digite o valor do prouto:"))
estado = input("Digite qual o estado(MG,SP,RJ,MS):")

if estado == "MG":
    res = valor*0.07 + valor
    print("O valor final fica:",res,"R$")
elif estado == "SP":
    res = valor*0.12 + valor
    print("O valor final fica:",res,"R$")
elif estado == "RJ":
    res = valor*0.15 + valor
    print("O valor final fica:",res,"R$")
elif estado == "MS":
    res = valor*0.08 + valor
    print("O valor final fica:",res,"R$")
else:
    print("Erro, estado Inválido:")    



