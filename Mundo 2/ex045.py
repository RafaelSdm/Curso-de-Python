import random
print("\033[1;31m-==-\033[m"*20)
print("\033[1;32m PEDRA PAPEL TESOURA \033[m")
print("\033[1;31m-==-\033[m"*20)

print("BEM VINDO AO JOGO, AQUI VOCE IRÁ ENFRENTAR A PRÓPRIA MAQUINA")
print("VOCE SAI JOGANDO! ESCOLHA PEDRA PAPEL OU TESOURA")

jogador = str(input()).upper()
lista = [1, 2, 3]

print("AGORA É A VEZ DO COMPUTADOR...")

escolha = random.choice(lista)

if escolha ==1:
    computador = "PAPEL"
elif escolha ==2:
    computador = "PEDRA"
else:
    computador ="TESOURA"
print("-==-"*20)
print("o computador escolheu {}".format(computador))
print("o jogador escolheu {}".format(jogador))
print("-==-"*20)

if  jogador =="PEDRA" and computador == "TESOURA":
    print("VOCE GANHOU!")
elif jogador == "PAPEL" and computador == "PEDRA":
    print("VOCE GANHOU!")
elif jogador == "TESOURA" and computador == "PAPEL":
    print("VOCE GANHOU!")
elif jogador == computador:
    print("O JOGO TERMINOU EMPATADO!")
else:
    print("GAME OVER :(")