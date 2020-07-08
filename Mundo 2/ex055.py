print("maior e menor peso")

maior_peso =0
menor_peso =0
for c in range(0,5):
    peso = float(input("informe o peso da {}° pessoa".format(c+1)))

    if c ==0:
        maior_peso = peso
        menor_peso = peso

    else:
        if peso >maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso


print("o maior peso encontrado foi de {} kg".format(maior_peso))
print("o menor peso encontrado foi de {} kg".format(menor_peso))