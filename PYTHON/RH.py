### exercício RH ###

nome = input("Digite seu nome completo:")
cargo = input("Digite seu cargo:")
email = input("Digite seu email:")
idade = int(input("Digite sua idade:"))
if(idade >= 18):
    print("Parabéns voçê passou para a próxima fase!!")
    curso = (input("Possui curso de qualificação na área: sim/não?"))
    if curso == "sim":
        print("Parabéns voçê passou para a próxima fase!!")
        nota = float(input("Digite a nota da prova:"))
        if(nota > 7.0):
            print("Parabéns voçê passou para a próxima fase!!")
        else:
            print("Obrigado por sua participação!!")
    else:
        print("Obrigado por sua participação!!")
else:
    print("Obrigado por sua participação!!")    


