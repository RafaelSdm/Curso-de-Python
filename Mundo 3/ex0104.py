def analise(dados, x =0):
    soma =0
    media =0
    analisador = {}
    if x ==0:
        analisador['total'] = len(dados)
        for c in range(0,len(dados)):
            if c ==0:
                maior = dados[c]
                menor = dados[c]
                analisador['maior'] = maior
                analisador['menor'] = menor
            else:
                if dados[c] > maior:
                    maior = dados[c]
                    analisador['maior'] = maior
                elif dados[c] < menor:
                    menor = dados[c]
                    analisador['menor'] = menor
        for c in range(0,len(dados)):
            soma = soma +  dados[c]
        media = soma / len(dados)
        analisador['media'] = media
    else:
        analisador['total'] = len(dados)
        for c in range(0,len(dados)):
            if c == 0:
                maior = dados[c]
                menor = dados[c]
                analisador['maior'] = maior
                analisador['menor'] = menor

            else:
                if dados[c] > maior:
                    maior = dados[c]
                    analisador['maior'] = maior
                elif dados[c] < menor:
                    menor = dados[c]
                    analisador['menor'] = menor
        for c in range(0,len(dados)):
            soma = soma + dados[c]
        media = soma / len(dados)

        if media >= 7:
            analisador['situação'] = "otima"
        elif media < 7 and media >=5:
            analisador['situação'] = "razoavel"
        else:
            analisador['situação'] = "pessima"

    print(analisador)



def linhas():
    print("-"*30)


notas = []


linhas()
print("validação do numero:")
linhas()

while True:
    notas.append(float(input("informe a nota do aluno:")))

    while True:
        resp = str(input("deseja continuar?")).upper().strip()[0]

        if resp in "SN":
            break
        else:
            print("dados invalidos!")
    if resp == "N":
        break
print(notas)
linhas()
resp1 = str(input("dejesa saber a situação?")).upper().strip()[0]
if resp1 == "N":
    analise(notas)
else:
    analise(notas,1)



