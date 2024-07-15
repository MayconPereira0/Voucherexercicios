def ver(A):
    if A > 0:
        return 'p'
    else:
        return 'n'

A = int(input("Digite o valor:"))

res = ver(A)

print("O número é",res)