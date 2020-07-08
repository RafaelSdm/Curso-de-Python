print("media dos valores")

i =1
j =1
soma =0
media =0
maior =0
menor =0

numero = int(input("informe um numero:"))
soma = soma + numero

while i != 0:

    if i == 1:
        maior = numero
        menor = numero

    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero


    resp = str(input("Deseja continuar? [S/N]")).upper()

    if resp == 'S':
        numero = int(input("informe um novo numero:"))
        j = j+1
        i = i+1
        soma = soma + numero

    else:
        i =0




media = soma / j

print("a media dos {} numeros digitados sao de {:.2f}".format(j,media))
print("o menor numero digitado foi {}".format(menor))
print("o maior numero digitado foi {}".format(maior))
