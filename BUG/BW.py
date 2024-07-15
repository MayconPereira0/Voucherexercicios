i = 0
soma = 0
while i < 10:
    try:
        x = int(input("Digite um número: "))
        soma += 1
        i += 1
    except: 
        print("VALOR INVALÍDO, TENTE NOVAMENTE!!")
print(soma)