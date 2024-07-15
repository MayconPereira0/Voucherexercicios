class Raio:
    def __init__(self,raio):
        self.raio = raio

    def imprimir_raio(self):
        print(f'\nO valor do raio é de: {self.raio}')
    def calcular_circulo(self):
        res = self.raio * 3.14 ** 2
        print(f"A área do círculo é de: {res:.2f}")
    def calcular_circun(self):
        res1 = self.raio * 3.14 * 2
        print(f"A circunferência é de: {res1:.2f}")
    
raio = float(input("Digite o valor do raio: "))

dados = Raio(raio)

dados.imprimir_raio()
dados.calcular_circulo()
dados.calcular_circun()