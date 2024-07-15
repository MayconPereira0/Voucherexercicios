horas = float(input("Digite as horas trabalhadas:"))

s = horas*40.50

if(s>2500):
    print("O sálario com descontos é:",s - (s*0.11),"R$")

else: 
    print("O sálario é:",s)

    