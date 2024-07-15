numeros = []
while True:
    nums = int(input("Digite um número: "))
    if nums < 0:
        break
    numeros.append(nums)
if numeros:
    print(f"O maior número digitado foi: {max(numeros)}")
else:
    print("Nenhum número válido foi digitado.")


