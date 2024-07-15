a = float(input("Digite um número:"))
b = float(input("Digite um número:"))
c = float(input("Digite um número:"))

if (a>0):
    if (b>0):
        print("Tudo ok para decolagem!")
    else:
        print("Tanque principal vazio; voando com combustível reserva!")
else:
    if(c>0):
       print("Foguete não tem piloto, mas há outros foguetes disponíveis!")
