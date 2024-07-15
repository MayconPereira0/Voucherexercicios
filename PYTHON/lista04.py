numbers = [28,11,2,4,6,99,55,56,57,27,68,40]
cont = 0
while cont < len(numbers):
    print("Valor do contador: ",cont,"Item da lista: ",numbers[cont])
    if numbers[cont] == 55:
        print("ACHAMOS O NÚMERO 55")
        break
    else:
        cont = cont + 1