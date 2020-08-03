lista = list()

for c in range(0,5):
    numero = int(input("informe um numero:"))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print("numero adicionada no final da fila")
    else:
        posicao =0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao,numero)
                print(f"o numero fornecido esta na posição {posicao} ")
                break
            posicao = posicao +1
print(f"os numeros indicados na ordem crescente é de {lista}")