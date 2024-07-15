h = float(input("Digite sua altura:"))
sex = str(input("Informe seu sexo (M ou F):"))

if sex.upper() == "M":
    peso_ideal = (72.7 * h) - 58
    print("O peso ideal para um homem com altura", h, "m é:", peso_ideal, "kg")

elif sex.upper() == "F":
    peso_ideal = (62.1 * h) - 44.7
    print("O peso ideal para uma mulher com altura", h, "m é:", peso_ideal, "kg")   

