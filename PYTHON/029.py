ano = int(input("Digite o ano: "))
bissexto = (ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0))
print(f"{ano} {'é' if bissexto else 'não é'} um ano bissexto.")
