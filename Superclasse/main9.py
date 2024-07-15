from Compra import Compra
from Compra import Avista
from Compra import Parcelada

Compra_avista = Avista(1, "Notebook", 3000.0, 10)
Compra_parcelada = Parcelada(2, "Smartphone", 1500.0, 12)

Compra_avista.calcular_valor_com_desconto()
Compra_parcelada.calcular_valor_parcela()

