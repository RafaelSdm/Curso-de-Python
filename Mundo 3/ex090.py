print("avaliacao do aluno:")

dicionario = {}
dicionario['nome'] = str(input("infome o nome do aluno:"))
dicionario['nota1'] = float(input("informe a sua primeira nota:"))
dicionario['nota2'] = float(input("informe a sua segunda nota:"))

media = (dicionario['nota1'] + dicionario['nota2']) /2
#print(dicionario)
print(f"a media do aluno {dicionario['nome']} é de {media}")
print("SITUAÇAO...")
if media < 4.5:
    print(f"o aluno {dicionario['nome']} esta refrovado!")
elif media > 4.5 and media <= 6:
    print(f"o aluno {dicionario['nome']} esta de recuperação")
else:
    print(f"o aluno {dicionario['nome']} esta aprovado!")