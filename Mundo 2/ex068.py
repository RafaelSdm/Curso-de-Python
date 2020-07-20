from time import sleep
from random import randint
print("jogo do par ou impar")
cont =0
while True:
    numero = int(input("Informe um numero:"))
    print("agora é a vez do computador escolher...")
    print("processando...")
    lista = randint(0, 10)
    computador = lista
    sleep(0.5)
    print("o computador acabou de escolhaer seu numero")
    escolha = str(input("voce deseja escolher par ou impar? [P/I]")).upper()

    soma = numero + computador

    if soma %2 ==0 and escolha == "P":
        print("_-_-"*12)
        print(f"parabens! voce venceu a maquina!\n voce digitou {numero} e o computador {computador} \n a soma deu {soma} que resultou em par")
        print("-_-_"*12)
        soma = 0
        cont = cont +1
    elif soma %2 != 0 and escolha == "I":
        print("|o|"*12)
        print(f"parabens! voce venceu a maquina!\n voce digitou {numero} e o computador {computador} \n soma deu {soma} que resultou em impar")
        print("|o|"*12)
        soma =0
        cont = cont +1
    else:
        print("a maquina vennceu!")
        break
print(f"game over otario \nvoce conseguiu ganhar {cont} do computador ")