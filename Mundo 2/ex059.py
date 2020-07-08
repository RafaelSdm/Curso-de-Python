print("CALCULADORA")

c = 1

while c != 5:
    resultado =0
    print("-"*20)
    print("[1] soma")
    print("[2] subtração")
    print("[3] multiplicação")
    print("[4] divisão")
    print("[5] Para fechar o programa")
    print("-"*20)
    c = int(input("informe o que deseja calcular:"))
    if c ==5:
        print("Voce saiu...")
        c ==5

    n1 = float(input("agora informe o primeiro numero:"))
    n2 = float(input("informe o segundo numero:"))

    if c == 1:
        resultado = n1 + n2
        print("o resultado da soma de {} e {} é de {:.2f}".format(n1,n2,resultado))
    elif c ==2:
        resultado = n1 - n2
        print("o resultado da subtrçõa ´de {} e {} é de {:.2f}".format(n1,n2,resultado))
    elif c ==3:
        resultado = n1 * n2
        print("o resultado da multiplicação de {} e {} é de {:.2f}".format(n1,n2,resultado))
    elif c == 4:
        resultado = n1 / n2
        print("o resultado da divisão entre {} e {} é de {:.2f}".format(n1,n2,resultado))
    else:
        c ==5
print("Fim da calculadora")