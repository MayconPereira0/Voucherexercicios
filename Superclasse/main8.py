from Imovel import Imovel
from Imovel import Casa

casa = Casa("111",1000,800,True,True,True)

casa.getIPTU()

novo_aluguel = float(input("Digite o valor do novo aluguel: "))
casa.setValor_Aluguel(novo_aluguel)


