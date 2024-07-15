dias_da_semana = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado"
}

dia = int(input("Digite um número entre 1 e 7:"))

if dia >= 1 and dia <= 7:
    print("O dia da semana correspondente ao número", dia, "é", dias_da_semana[dia])

