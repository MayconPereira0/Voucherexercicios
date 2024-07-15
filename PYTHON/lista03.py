numeros = [2,3,4,11,5]
i = 0

while i < len(numeros):
    print(i)
    if numeros[i] == 11:
        print('encontramos o número 11!')
        break
    else:
        i = i + 1