class Imovel():
    def __init__(self,InscricaoMunicipal,Valor_aluguel,IPTU):
        self.InscricaoMunicipal= InscricaoMunicipal
        self.Valor_aluguel = Valor_aluguel
        self.IPTU= IPTU

    def getIPTU(self):
        print(f"O valor do IPTU é {self.IPTU}R$")


    def setValor_Aluguel(self,novo_aluguel):
        self.Valor_aluguel= novo_aluguel
        print(f"Novo valor do aluguel é: {self.Valor_aluguel}")



class Casa(Imovel):
    def __init__(self, InscricaoMunicipal, Valor_aluguel, IPTU,churasqueira,sala_de_estar,quarto):
        super().__init__(InscricaoMunicipal, Valor_aluguel, IPTU)
        self.churasqueira= churasqueira
        self.sala_de_estar=sala_de_estar
        self.quarto= quarto

    

class Apartamento(Imovel):
    def __init__(self, InscricaoMunicipal, Valor_aluguel, IPTU,nome_porteiro,modelo_elevador,numero_apt):
        super().__init__(InscricaoMunicipal, Valor_aluguel, IPTU)
        self.nome_porteiro= nome_porteiro
        self.modelo_elevador= modelo_elevador
        self.numero_apt=numero_apt


class Terreno(Imovel):
    def __init__(self, InscricaoMunicipal, Valor_aluguel, IPTU,metros_quadrados):
        super().__init__(InscricaoMunicipal, Valor_aluguel, IPTU)
        self.metros_quadrados=metros_quadrados


class Chacarra(Imovel):
    def __init__(self, InscricaoMunicipal, Valor_aluguel, IPTU,piscina,gado):
        super().__init__(InscricaoMunicipal, Valor_aluguel, IPTU)
        self.piscina= piscina
        self.gado=gado