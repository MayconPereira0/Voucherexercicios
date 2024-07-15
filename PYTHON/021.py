n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
n3 = float(input("Digite a terceira nota:"))

pl = 2
ps = 3
pf = 5

media = (n1*pl + n2*ps + n3*pf) / (pl+ps+pf)

if media <= 2.9:
    print("O aluno está reprovado!")

elif media >= 3.0 and media <= 5.9:
    print("O aluno está de recuperação!")

else:
    print("O aluno está aprovado!")


