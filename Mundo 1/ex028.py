import random
numero = str(input("diga um  numero de 1 a 5:"))
lista = [1,2,3,4,5]

computador = random.choice(lista)
print("o computador escolheu o numero:{}".format(computador))

if numero == computador:
    print("Parabens,voçe pensa como uma maquina")
else:
    print("seu fraco QI mostra sua incompetencia")