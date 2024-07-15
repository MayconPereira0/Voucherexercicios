sal = 4000
aumento = (1.5 / 100)*sal
sal += aumento
ano = 2020

while ano <= 2024:
    print(sal)
    aumento *= 2
    sal += aumento
    ano += 1

