def calc(horas,sal):

    if horas <= 40:
        s_total = horas * sal
    else:
        h_extras = horas - 40
        pagam_h_extras = h_extras * (sal*1.5)
        sal_base = 40 * sal
        s_total = sal_base + pagam_h_extras
    return s_total

h = float(input("Digite o número de horas trabalhadas: "))
sal = float(input("Digite o salário por hora: "))

salario = calc(h,sal)

print(f"salario total é R${salario:.2f}")
