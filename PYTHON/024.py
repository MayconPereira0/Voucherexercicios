B1 = float(input("Digite a base maior do trapézio:"))
B2 = float(input("Digite a base menor do trapézio:"))
A = float(input("Digite a altura do trapézio:"))

a = (B1 + B2) * A / 2

if B1 < 0 and B2 < 0:
    print("A área do trapézio é:",a)
