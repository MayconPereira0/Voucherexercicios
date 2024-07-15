def media_num(*args):
    soma = sum(args)
    quant = len(args)
    return soma/quant
print(media_num(1,2,3))