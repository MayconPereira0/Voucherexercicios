numero = int(input("Digite um número inteiro entre 100 e 9999: "))


if 100 <= numero <= 9999:
    numero_str = str(numero)
    print("Os algarismos que compõem o número são:")
    for algarismo in numero_str:
        print(algarismo)
