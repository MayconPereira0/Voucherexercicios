def calculartempo(tempo_min):
    valor_min = 9.00
    valor_extra = 1.50
    if tempo_min < 15:
        return 0.0
    horas_completas = tempo_min // 60
    min_restante = tempo_min % 60

    if min_restante > 0:
        horas_completas += 1

    if horas_completas == 1:
        total = valor_min
    else:
        total = valor_min + (horas_completas - 1) * valor_extra
    return total

tempo_utilizadom = int(input("Digite o tempo em minutos:"))

horas_totais = tempo_utilizadom / 60 
valor_total = calculartempo(tempo_utilizadom)
pis = (0.33/100) * valor_total
cofins = (0.20/100) * valor_total
icms = (17/100) * valor_total
impostos = (pis + cofins + icms)


print(f"Tempo {horas_totais} horas \n PIS R$ {pis:.2f} \n COFINS R$ {cofins:.2f} \n ICMS R$ {icms:.2f} \n IMPOSTOS R$ {impostos:.2f} \n TOTAL R$ {valor_total:.2f}")
 
