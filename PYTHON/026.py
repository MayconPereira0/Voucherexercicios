A = float(input("Digite um valor:"))
B = float(input("Digite um valor:"))
C = float(input("Digite um valor:"))

if A < B + C and B < A + C and C < A + B:

    if A == B == C:
            print ("Equilátero")
        # Verificar se é isósceles
    elif A == B or A == C or B == C:
            print ("Isósceles")
        # Caso contrário, é escaleno
    else:
        print ("Escaleno")

else:
    print ("Não forma um triângulo")
