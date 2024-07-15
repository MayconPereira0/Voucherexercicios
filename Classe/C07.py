class Triangulo:
    def __init__(self,LadoA,LadoB,LadoC):
        self.LadoA = LadoA
        self.LadoB = LadoB
        self.LadoC = LadoC
    def calcular_perimetro(self):
        p = self.LadoA + self .LadoB + self.LadoC
        print(f"O perímetro do triângulo é de: {p}")
    def maior_lado(self):
        maior = max(self.LadoA,self.LadoB,self.LadoC)
        print(f"O maior lado do triângulo é: {maior}")
    def calcular_area(self,altura):
        a = (self.LadoA*altura)/2
        print(f"A área do triângulo é de: {a}")

l1 = float(input("Digite o lado 1: "))
l2 = float(input("Digite o lado 2: "))
l3 = float(input("Digite o lado 3: "))

dados = Triangulo(l1,l2,l3)

altura = float(input(f"Digite a altura do triângulo: "))
dados.calcular_area(altura)

dados.calcular_perimetro()
dados.maior_lado()