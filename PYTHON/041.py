a = -3
b = 5
c = -1
delta = b**2 - 4*a*c
print(f"delta igual a {delta}")
x1 = (-b + (delta **(1/2))) / 2*a
x1n = round(x1, 2)
print(x1n)
x2 = (-b - (delta ** (1/2))) / 2*a
x2n = round(x2, 2)
print(x2n)
if(delta < 0):
    print("Não existe delta")
elif(delta == 0):
    print("Raiz única")
elif(delta >- 0):
    print("Duas raízes rais")

