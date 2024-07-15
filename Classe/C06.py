class Agenda:
    def __init__(self,dia,mes,ano,anotacao):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao
    
    def validar_data(self):
        print(f"{self.dia}/{self.mes}/{self.ano}")

    def anotar_tarefa(self):
        anotacao = self.anotacao
        print(f"Voçê possui a seguinte anotação: {anotacao}")

print("Digie o dia, mês e ano da agenda!")
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
anotacao = input("Digite o que deseja anotar: ")

dados = Agenda(dia,mes,ano,anotacao)

dados.validar_data()
dados.anotar_tarefa()
