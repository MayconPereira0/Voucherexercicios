n1 = int(input("Digite um número:"))
n2 = int(input("Digite um número:"))

print ('Maior número da lista:', max(n1,n2))

if n1 > n2:
    diferenca = n1 - n2
    print("A diferença entre os números é:", diferenca)
elif n2 > n1:
    diferenca = n2 - n1
    print("A diferença entre os números é:", diferenca)