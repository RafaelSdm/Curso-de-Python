print("Analise de compras...")
i =0
soma = 0
j =0
while True:
    nome = str(input("informe o nome do produto:"))
    compra = float(input("Informe o valor do produto:"))
    soma = soma + compra

    if compra > 1000:
        j = j+1
    if i == 0:
        maior = compra
        maior_nome = nome

    if i != 0 and compra > maior:
        maior = compra
        maior_nome = nome

    while True:
        resp = str(input("deseja informar mais algum produto?")).upper()

        if resp == "N" or resp == "S":
            break
        elif resp != 'S' and resp != 'N':
            print("opcao invalida!")
    if resp == 'N':
        break
    else:
        i = i+1

print(f"dados informados: \n o maior produto é o {maior_nome} com o valor de {maior}\n e sua compra deu no total de R${soma}\n sendo que {j} deles sao mais de R$1000,00e")
