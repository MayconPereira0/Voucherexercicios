n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))

if(n1 and n2 > 0.0):
    media = (n1 + n2)/2
    print("A média das notas é:", media)

else:
    print("As notas não atigem o valor mínimo")