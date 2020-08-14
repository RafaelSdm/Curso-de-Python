def linhas():
    print("-" * 38)


def leiaInt(msg):
    validacao = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            validacao = True
        else:
            print("valor informado nao é um numero inteiro")
        if validacao:
            break
    return valor


linhas()
print("analise de um numero inteiro")
linhas()

n = leiaInt("informe um numero:")
print(f"voce acabou de informar o numero {n}")


