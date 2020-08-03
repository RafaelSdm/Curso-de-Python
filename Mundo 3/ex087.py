from random import randint
print("-"*30)
print("JOGO DA MEGA SENA")
print("-"*30)
mega = list()

sorteio = int(input("informe quantas vezes o jogo ira ser sorteado:"))

for c in range(0,sorteio):
    for c in range(0,6):
        sorteado = randint(0,60)

        mega.append(sorteado)

print(f"numeros sorteados \n\n {mega}")