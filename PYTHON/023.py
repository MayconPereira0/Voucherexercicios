meses_do_ano = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

mes = int(input("Digite um número entre 1 e 12:"))

if mes >= 1 and mes <= 12:
    print("O mes do ano correspondente ao número", mes, "é", meses_do_ano[mes])