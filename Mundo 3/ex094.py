print("analise do grupo de pessoas...")
pessoa = {}
grupo = []
soma = media =0
contador =0
while True:
    print("---"*30)
    pessoa['nome'] = str(input("informe o nome:"))
    contador = contador+1
    while True:
        pessoa['sexo'] = str(input("informe o sexo:")).strip().upper()[0]
        if pessoa['sexo'] in "MF":
            break
        else:
            print("invalidos seus digitos")
    pessoa['idade'] = int(input("informe sua idade:"))
    soma = soma + pessoa['idade']
    grupo.append(pessoa.copy())
    pessoa.clear()
    print("---"*30)
    while True:
        resp = str(input("deseja informar mais alguem?")).strip().upper()[0]
        if resp in "SN":
            break
        else:
            print("dados infrmados invalidos!")
    if resp == 'N':
        break
media = soma / contador
print(grupo)
print(media)
print("ANALISE DOS DADOS INFORMADOS:")
print(f"foram informados {contador} pessoas")
print(f"A media das idades entre as pessoas é de {media:5.2f}")
print("mulheres cadastradas...")
for c in grupo:
    if c['sexo'] == 'F':
        print(f"{c['nome']} ",end="")
print()
print("dados das pessoas com idade mais avançada...")

for c in grupo:
    if c['idade'] > media:
        print('   ',end="")
        for i, j in c.items():
            print(f"{i} == {j}",end="")
        print()





