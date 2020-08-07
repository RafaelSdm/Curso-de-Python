from random import randint
def linhas():
    print("-"*30)
def sorteio():
    print("lista sorteada:")
    for c in range(0,5):
        num = randint(0,10)
        lista.append(num)
        print(f" {lista[c]} ",end='')
    print()
def pares():
    soma =0
    for c in range(0,5):
        if lista[c] %2 ==0:
            soma = soma + lista[c]
    print(f"a soma dos numeros pares da lista é de {soma}")



#funcao principal

lista = []

linhas()
print("somando os numeros pares da lista")
linhas()
sorteio()
pares()

