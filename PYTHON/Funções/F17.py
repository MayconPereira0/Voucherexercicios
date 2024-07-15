def dados(**kwargs):
    for chave, item in kwargs.items():
        print(f"{chave} : {item}")

dados(firstname_is = "Maycon", lastname_is = "Ruan", Email = "maycon@123", Coutry_is = "Campo Grande", Age_is = "18", phone = "0000")