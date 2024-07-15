def lista(lista):
    for i, elemento in enumerate(lista, start=1):
        print(f"{i}, {elemento}")
lista1 = ["Pera", "Uva", "Morango"]
resp = lista(lista1)

def imprime(lista):
    cont = 0
    while cont < len(lista):
        print(f"{cont+1}, {lista[cont]}")
        cont += 1
lista = ["Pera", "Uva", "Morango"]

imprime(lista)