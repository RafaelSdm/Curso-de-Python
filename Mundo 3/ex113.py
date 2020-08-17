def linhas():
    print('-'*30)

def inteiro(txt):
    while True:
        try:
            numero = int(input(txt))
        except Exception:
            print(linhas())
            print("valor informado nao bate com o que se pede:")
            print(linhas())
        else:
            return numero
            break

def flutuante(txt):
    while True:
        try:
            num = float(input("informe um numero flutuante:"))
        except Exception:
            print(linhas())
            print("valor informado nao bate com o que se pede")
            print(linhas())
        else:
            return num
            break





linhas()
print("tratamento de erros com numeros inteiros e de tipo float")
linhas()

numint = inteiro("informe um numero:")
print(f"o numero informado foi o {numint}")

numfloat = flutuante("informe um valor:")
print(f'o valor informado flutuante é o {numfloat}')




