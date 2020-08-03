print("matriz 3 x 3")
matriz = list()
matrizFinal = list()
contador =0
print("informe os valores da matriz:")

for c in range(0,9):
    numero = int(input("informe um numero"))


    while True:
        if contador <3:
            matrizFinal.append(numero)
            contador = contador +1
        else:
            contador = 0
            break

print("matriz formada:")

for c in matrizFinal:
    print(f"{c}")

