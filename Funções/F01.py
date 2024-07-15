def pot(base, n):
    for i in range(1, n + 1):
        resultado = base ** i
        print(f"{resultado}")

pot(2, 3)