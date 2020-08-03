print("analise dos numeros da lista:")
print("-"*20)
contador =1
lista = list()
while True:
    lista.append(int(input("informe um numero:")))



    while True:
        resposta = str(input("deseja informar mais algum numero:")).strip().upper()[0]
        if resposta in "SN":
            break
        else:
            print("dados informados invalidos!")
    if resposta == "N":
        break
    else:
        contador += 1

print(f"voce informou {contador} numeros na lista")

print("\n\nlista dos numeros informados:")

for c in lista:
    print(f" {c} ",end="")

print("\n\nordem decrescente dos numeros:")

lista.sort(reverse=True)
print(f" {lista} ")

print("\n\nanalise do numero 5 na lista:")

if 5 in lista:
    print("o numero 5 aparece na lista")
else:
    print("o numero 5 nao aparece na lista")

