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

def resumo(num):
    print('-'*31)
    print("analise do dinheiro proposto:")
    print('-'*31)
    print(f"valor informado: \t{dobro(num/2)}")
    print(f"Dobro do valor: \t{dobro(num,True)}")
    print(f'metade do valor: \t{metade(num,True)}')
    print(f"aumento de 10%: \t{porcentagem(num,True)}")
    print(f"redução de 13%: \t{reduzindo(num,True)}")