print("valores dos numeros pares e impares:")

lista = [[],[]]
numero =0

for c in range(0,7):
    numero = int(input(f"informe o {c+1}° numero:"))

    if numero %2 ==0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)

print("Dados os numeros informados:")
print("lista dos numeros pares em ordem crescente:")
lista[0].sort()
for c in lista[0]:
    print(f"[{c}]",end="")
print()
print("lista dos numeros impares em ordem crescente:")
lista[1].sort()
for c in lista[1]:
    print(f"[{c}]",end="")




