ganho = float(input("Digite o ganho por hora:"))
horas = float(input("Digite as horas trabalhadas no mês:"))

bruto = ganho*horas
inss = 0.08*bruto
sindicato = 0.05*bruto
ir = bruto*0.11
liquido = bruto - (inss+sindicato+ir)
print(f"O salário bruto é {bruto}R$, e o salário líquido é:{liquido}R$\nPagou:\n{inss}R$ de INSS\n{sindicato}R$ de Sindicato\n{ir}R$ de Imposto de reda")
