def dobro(num, formato = False):
    resp = num *2
    return resp if formato is False else moeda(resp)


def metade(num,formato = False):
    resp = num / 2
    return  resp if formato is False else moeda(resp)


def porcentagem(num,formato = False):
    resp = num + (num * 10/100)
    return resp if formato is False else moeda(resp)

def reduzindo(num,formato = False):
    resp = num - (num * 13/100)
    return resp if formato is False else moeda(resp)

def moeda(num,moeda='R$'):
    return f"{moeda}{num:.2f}".replace('.',',')