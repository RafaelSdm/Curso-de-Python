import random
print("numeros aleatorios dentro da tupla:")
maior = 0
menor =0
numeros = (random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50),random.randint(0,50))
print("numeros gerados aleatoriamente:")
for c in range(0,5):
    print(f"{numeros[c]}")
    if c == 0:
         maior = numeros[c]
         menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        elif numeros[c] < menor:
            menor = numeros[c]
print(f"o maior numero da lista é o {maior} e o menor é o numero {menor}")
print("maiores numeros de um maneira diferente:")
print(f"o maior numero é o {max(numeros)} e o menor numero é o {min(numeros)}")


