numero = int(input("informe um numero:"))
soma =0
j=0
while numero != 999:
    soma = soma + numero
    j = j +1

    numero = int(input("informe outro numero:"))
print("a soma dos {} digitados numeros foi de {}".format(j,soma))