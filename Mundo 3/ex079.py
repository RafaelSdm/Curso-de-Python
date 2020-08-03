print("valores ordenados:")
print("-"*30)

lista = list()
cont =0

while True:
    numero = int(input("informe um numero:"))
    if cont == 0:
        lista.append(numero)
    elif cont > 0:
        if numero in lista:
            print("numero digitado ja esta na lista")
        else:
            lista.append(numero)

    while True:
        resposta = str(input("deseja infrmar outro numero?")).strip().upper()[0]

        if resposta in "SN":
            cont = cont +1
            break
        else:
            print("valores informados invalidos!")
    if resposta == "N":
        break

print("lista dos numeros informados:")
for c in lista:
    print(f" {c} ",end="")
print("\n\ncolocando a lista em ordem crescente:")

lista.sort()
print(f" {lista} ")














#for c in range(0,4):
 #   numero = int(input("numero:"))
  #  baba.append(numero)


#print("os numeros da lista sao: {}".format(baba))

