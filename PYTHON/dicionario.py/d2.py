amigos = {
    "Maycon": "18",
    "Arthur": "17",
    "Leandro": "19"
}

for nomes in amigos:
    print(nomes, amigos[nomes])

novo = input("Digite o nome: ")

if novo in amigos:
    print("Amigo já está")
else:
    print("Amigo não está")