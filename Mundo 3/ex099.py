def linhas():
    print("-"*30)
def cont(num):
    print("dada a lista")
    i =0
    for c in num:
        print(f" {c} ",end="")
    print(f"foram informados {len(lista)} numeros ")

    while i < len(lista):
        if i ==0:
            maior = lista[i]
        else:
            if lista[i] > maior:
                maior = lista[i]
        i = i +1
    print(f"o maior numero da lista é o {maior} ")

lista = []
linhas()
print("analisador do maior valor na lista...")
linhas()

while True:
    lista.append(int(input("informe um numero:")))
    while True:
        resp = str(input("deseja continuar?")).strip().upper()[0]
        if resp in 'SN':
            break
        else:
            print("dados invalidos")


    if resp == "N":
        break
linhas()
print("analise da lista...")


cont(lista)
