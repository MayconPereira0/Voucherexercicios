def somaimposto(taxaimposto,custo):
    somaimposto = taxaimposto * custo/100
    somaimposto = somaimposto+custo
    return somaimposto

taxaimposto = float(input("Digite o taxa do imposto em %:"))
custo  = float(input("Digite o custo:"))

resp = somaimposto(taxaimposto,custo)

print(resp)