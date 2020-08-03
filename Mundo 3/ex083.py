expressao = str(input("informe sua expressao"))
contD =0
contE =0
#expressao.append(str(input("informe sua expressao:")))

for c in range(0,len(expressao)):
    if expressao[c] == '(':
        contD = contD + 1
    elif expressao[c] ==  ')':
        contE = contE +1

print(f"na expressao possui {contE} de esquerda e {contD} de direita de tamanho {len(expressao)} ")

if contE == contD:
    print("dadas as expressoes,tudo indica que sao validas!")
else:
    print("expressoes nao validas!")