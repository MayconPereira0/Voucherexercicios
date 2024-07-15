### Crie um programa, utilizando dicionarios, que solicite ao usuario inserir quatro notas e mostre na tela as notas e a media##
notas = {}

for i in range(4):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas[f"Nota {i+1}"] = nota

media = sum(notas.values()) / 4

print("\nNotas inseridas:")
for key, value in notas.items():
    print(f"{key}: {value}")

print(f"\nMédia das notas: {media:.2f}")

