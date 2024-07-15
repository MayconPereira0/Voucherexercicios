traducao = {
    "hello":"Hola",
    "tanks":"tankes"
}

resp = input("Digite a palavra que deseja traduzir:")

if resp in traducao:
    print(traducao[resp])
else:
    print("Palavra não traduzida")