print("Maiores e menores valores da lista:")
print("-"*20)

lista = list()

for c in range(0,5):
    lista.append(int(input(f"informe o {c+1} valor:")))
print("os valores informados foram:")
for c in range(0,5):
    print(f" {lista[c]} ",end="")
#informaçoes dos maiores e menores numeros:

for c in range(0,5):
    if c ==0:
        maior = lista[c]
        menor = lista[c]
        posicaoM = c
        posicaoMe = c
    else:
        if lista[c] > maior:
            maior = lista[c]
            posicaoM = c
        elif lista[c] < menor:
            menor = lista[c]
            posicaoMe = c
print(f"\no maior numero da lista é o {maior} na {posicaoM +1} posiçaõ \no menor valor é o {menor} na posição {posicaoMe+1}")