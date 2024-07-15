num = int(input("Digite um número:"))

divisor = 2

primo = True

while divisor <= num ** 0.5:
    if num % divisor == 0:
        primo = False
        break
    divisor += 1
    
if primo:
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")