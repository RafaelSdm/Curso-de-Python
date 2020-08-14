def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg))
        if entrada.isalpha():
            print("invalido")
        else:
            valido = True
            return float(entrada)
