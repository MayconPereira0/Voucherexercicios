km = float(input("Digite a distância em Km:"))
l = float(input("Digite quantos litros o carro gastou:"))

Kml = km/l

if Kml < 8:
    print("Venda o carro!")
elif Kml >= 8 and Kml < 14:
    print("Econômico!")
elif Kml > 12:
    print("Super econômico!")


