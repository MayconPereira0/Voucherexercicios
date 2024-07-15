class Nota_Fiscal:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, valor_produtos, icms, frete, ipi):
        self.numero = numero
        self.tipo = tipo  # Entrada ou Saída
        self.serie = serie  # 1, 2 ou 3
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.valor_produtos = valor_produtos
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_total = 0
    def obterNumero(self):
        print(f"O número é: {self.numero}")
    def obterDataEmissao(self):
        print(f"{self.data}")
    def alterarRazaoSocial(self,alteraRs):
        self.razao_social = alteraRs
    def calcularValorTotal(self):
        self.valor_total = sum([self.valor_produtos,self.frete,self.ipi,self.icms])
        return self.valor_total

numero = input("Digite o número da nota fiscal: ")
tipo = input("Digite o tipo da nota fiscal (Entrada ou Saída): ")
serie = int(input("Digite a série da nota fiscal (1, 2 ou 3): "))
cnpj = input("Digite o CNPJ: ")
razao_social = input("Digite a razão social: ")
data = input("Digite a data de emissão da nota fiscal (formato YYYY-MM-DD): ")
valor_produtos = float(input("Digite o valor dos produtos: "))
icms = float(input("Digite o valor do ICMS: "))
frete = float(input("Digite o valor do frete: "))
ipi = float(input("Digite o valor do IPI: "))

nota = Nota_Fiscal(numero,tipo,serie,cnpj,razao_social,data,valor_produtos,icms,frete,ipi)

print("\n********** NOTA FISCAL **********")
print("Número:", nota.obterNumero())
print("Tipo:", nota.tipo)
print("Série:", nota.serie)
print("CNPJ:", nota.cnpj)
print("Razão Social:", nota.razao_social)
print("Data de Emissão:", nota.obterDataEmissao())
print("================================")
print("ITENS:")
print(f"Valor dos Produtos: R$ {nota.valor_produtos:.2f}")
print(f"ICMS: R$ {nota.icms:.2f}")
print(f"Frete: R$ {nota.frete:.2f}")
print(f"IPI: R$ {nota.ipi:.2f}")
print("================================")
print(f"VALOR TOTAL: R$ {nota.calcularValorTotal():.2f}")
print("********************************")