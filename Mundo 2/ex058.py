from random import choice,randint
from time import sleep

lista = randint(0,10)
i=0
c =1
print("JOGO DA ADIVINHAÇÃO")

print("Bem vindo ao jogo! Tente adivinhar o numero do qual o computador esta pensando...")

print("\n\na saída é feita pelo computador...")
computador = lista
print("processando...")
sleep(2)
print("O computador ja escolheu seu numero, agora é a sua vez \n Escolha um numero de 1 a 10...")

while c ==1:
    numero = int(input("Informe o numero:"))
    i = i +1
    if numero == computador:
        c =c+1
    else:
        print("OPS! Parece que não foi esse o numero fornecido pelo computador :(")
        if numero < computador:
            print("DICA: o numero do computador é maior que o {}".format(numero))
        else:
            print("DICA: o numero do computador é menor que {}".format(numero))
        c ==1
print("\nO COMPUTADOR ESCOLHEU O NUMERO {}".format(computador))
print("\nPARABENS VOCE CONSEGUIU ACERTAR NA SUA {}°TENTATIVA".format(i))

