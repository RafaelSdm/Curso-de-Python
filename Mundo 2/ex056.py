soma =0
media =0
maior_id_m =0
nomevelho =''
mulher =0
for c in range(1,5):
    print("{} pessoa".format(c))
    nome = str(input("informe o nome:")).strip()
    idade = int(input("informe a idade:"))
    sexo = str(input("sexo: M/F")).strip()

    soma = soma + idade


    if c ==1 in "Mm":
        maior_id_m = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maior_id_m:
        maior_id_m = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        mulher = mulhar +1



media = soma/4

print("a media das idades deste grupo é {}".format(media))
print("o homem mais velho tem{} anos e se chama {}".format(maior_id_m,nomevelho))
print("existe {} mulheres deste grupo com mais de 20 anos".format(mulher))
