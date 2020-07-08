print("\033[1;91m-==-\033[m"*20)
print("\033[1;91m ESCOLA ESTADUAL CHIQUINHO DE PAIVA\033[m")
print("\033[1;91m-==-\033[m"*20)

nota1 = float(input("Informe a nota do 1°bimestre"))
nota2 = float(input("informe a nota do 2° bimestre"))

media = (nota1 + nota2) / 2

print("o aluno esta com a media de {} pontos".format(media))

if media >= 7.0:
    print("EXCELENTE ALUNO! APROVADO NA DISCIPLIANA!")
elif media >= 5.0 and media <= 6.9:
    print("RECUPERAÇÃO!")
else:
    print("VOCE ESTA REPROVADO!")