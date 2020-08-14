def dobro(num):
    return num * 2


def metade(num):
    return  num / 2


def porcentagem(num):
    return  num + (num * 10/100)

def reduzindo(num):
    return  num - (num * 13/100)

def moeda(num,moeda='R$'):
    return f"{moeda}{num:.2f}".replace('.',',')