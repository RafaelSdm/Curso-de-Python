from random import randint
from time import sleep
print("jogo da mega senha")
lista = []
sorteio =[]
contador =0
jogo = int(input("informe quantas vezes voce quer jogar na mega sena:"))

for c in range(0,jogo):
    while contador <=6:
        numero = randint(1,60)
        if numero not in lista:
         lista.append(numero)
         contador = contador + 1

    lista.sort()
    sorteio.append(lista[:])
    lista.clear()
    contador =0
print(f"lista dos {jogo} jogos sorteados:")

for c, i in enumerate(sorteio):
    print(f" {i}")
    sleep(1.3)





