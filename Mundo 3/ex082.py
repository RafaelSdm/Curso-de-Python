print("lista dos numeros pares e impares")
print("-"*20)
lista = list()
par = list()
impar = list()

while True:
    lista.append(int(input("informe um numero:")))

    while True:
        resposta = str(input("deseja informar mais algum numero:")).strip().upper()[0]

        if resposta in "SN":
            break
        else:
            print("dados informados invalidos")
    if resposta == "N":
        break


print("segue a lista informada abaixo:")

for c in lista:
    print(f" {c} ",end="")
print("\n\nanalisando os numeros e colocando em listas de pares e impares:")

for c in range(0, len(lista)):
    if lista[c] %2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])
print("lista dos numeros pares da lista:")

for c in par:
    print(f" {c} ",end="")
print("\nlista dos numeros impares da lista:")

for c in impar:
    print(f" {c} ",end="")