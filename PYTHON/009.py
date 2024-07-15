import math
n1=float(input("Digite um número:"))
if(n1>=0):
    raiz_quadrada = math.sqrt(n1)
    print("A raiz quadrada de", n1, "é", raiz_quadrada)
else:
    print("O número ao qudrado de" , n1, "é", n1**2)