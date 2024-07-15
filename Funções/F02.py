from datetime import datetime

def data_atual(data):
    try:
        # Fazendo o parsing da string para um objeto datetime
        data_obj = datetime.strptime(data, '%d/%m/%Y')
        # Formatando a data para o formato desejado
        data_formatada = data_obj.strftime('%d de %B de %Y')
        print(data_formatada)
    except ValueError:
        print("Formato de data inválido. Use o formato dd/mm/aaaa.")

data_str = input("Digite a data (formato dd/mm/aaaa): ")

data_atual(data_str)