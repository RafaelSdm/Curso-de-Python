n1 = int(input("digite o primeiro numero:"))
n2 = int(input("digite o segundo numero:"))
n3 = int(input("digite o terceiro numero:"))

menor = n1
maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior= n3

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print("o maior numero da sequencia é {}".format(maior))
print("o menor numero da sequencia é {}".format(menor))

