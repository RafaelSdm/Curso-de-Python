print("identifição da maioridade: ")
cont = 0
for c in range(0,7):
    idade = int(input("informe a idade da {}°pessoa:".format(c+1)))

    if idade >= 21:
        cont = cont +1

print("dados mostram que {} pessoas possuem a maioridade, e {} ainda sao menores de idade".format(cont, 7 - cont))