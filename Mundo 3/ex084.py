from time import sleep
print("analise dos pesos:")
cadastro = list()
rascunho = list()
nomes = list()
nomesP = list()
maiorP = menorP =0
contador = 0
cont =0
while True:
    print("-"*30)
    rascunho.append(str(input("informe o seu nome:")))
    rascunho.append(float(input("Diga o seu peso:")))
    print("-"*30)
    contador = contador +1
    cadastro.append(rascunho[:])
    rascunho.clear()

    while True:
        resposta = str(input("\n\ndeseja informar mais alguem?")).strip().upper()[0]

        if resposta in "SN":
            break
        else:
            print("dados invalidos!")

    if resposta == "N":
        break


print("analisando a cobertura de dados:")
sleep(3)

for c in cadastro:
    if cont == 0:
        maiorP = c[1]
        menorP = c[1]
        cont += 1
    else:
        cont +=1

    if maiorP <= c[1]:
        maiorP = c[1]
        nomes.append(c[0])

    elif menorP >= c[1]:
        menorP = c[1]
        nomesP.append(c[0])

print(f"nessa analise foram feitas {contador} cadastros")
print(f"nomes da(s) pessoa(s) com maior peeso :({maiorP}kg)")
for c in nomes:
    print(f" {nomes}, ",end="")
print(f"\n\nnomes das pessoas com menos peso ({menorP})kg:")
for c in nomesP:
    print(f" {nomesP}, ",end="")


