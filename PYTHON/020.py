n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
n3 = float(input("Digite a terceira nota:"))

media = (((n1*1)+(n2*1)+(n3*2))/4) * 10

if(media>6.0):
    print("A média empoderada é:", media ,", O aluno está Aprovado")

else:
    print("A média empoderada é:", media ,", O aluno está Reprovado")
