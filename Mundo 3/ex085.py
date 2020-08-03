print("valores pares e impares:")
par = list()
impares = list()
listaFinal = list()
for c in range(0,7):
    numero = int(input("informe um numero:"))

    if numero %2 == 0:
        par.append(numero)
    else:
        impares.append(numero)

impares.sort()
par.sort()
listaFinal.append(par[:])
listaFinal.append(impares[:])

print("lista em ordem crescente dos numeros informados:")

for c in listaFinal:
    print(f" {c} ",end="")




