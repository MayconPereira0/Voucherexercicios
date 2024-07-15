class Compra:
    def __init__(self, numero, produto, valor):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = 0
    
    def calcular_valor_total(self):
        icms = 0.17 * self.valor
        frete = 0.05 * self.valor
        self.valor_total = self.valor + icms + frete
        return self.valor_total

class Avista(Compra):
    def __init__(self, numero, produto, valor, desconto):
        super().__init__(numero, produto, valor)
        self.desconto = desconto
    
    def calcular_valor_com_desconto(self):
        valor_total_com_impostos = self.calcular_valor_total()
        valor_com_desconto = valor_total_com_impostos * (1 - self.desconto / 100)
        print(f"Valor total da Compra à vista com desconto: R${valor_com_desconto:.2f}")

class Parcelada(Compra):
    def __init__(self, numero, produto, valor, numero_parcelas):
        super().__init__(numero, produto, valor)
        self.numero_parcelas = numero_parcelas
    
    def calcular_valor_parcela(self):
        valor_total_com_impostos = self.calcular_valor_total()
        valor_parcela = valor_total_com_impostos / self.numero_parcelas
        print(f"Valor de cada parcela na Compra parcelada: R${valor_parcela:.2f}")

