from datetime import date
print("-==-"*20)
print("selecao de idades para natação")
print("-==-"*20)

idade = int(input("Informe sua data de nascimento"))
ano = date.today().year
permissao = ano - idade

ida = ano - idade

print("o aluno tem {} anos".format(ida))

if permissao <=9:
    print("SEU MODULO É MIRIM")
elif permissao >= 10 and permissao <=14:
    print("SEU MODULO É INFANTIL")
elif permissao >= 15 and permissao <=19:
    print("SEU MÓDULO É JUNIOR")
elif permissao >= 20 and permissao <=20:
    print("SEU MODULO É SENIOR")
else:
    print("SEU MODULO É MASTER")