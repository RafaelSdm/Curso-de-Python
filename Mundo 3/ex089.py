print("medias dos alunos:")

lista = []

while True:
    nome = str(input("informe o nome do aluno:"))
    nota1 = float(input("informe a primeira nota do aluno:"))
    nota2 = float(input("informe a segunda nota do aluno:"))
    media = (nota1 + nota2) /2

    lista.append([nome,[nota1,nota2],media])

    while True:
        resp = str(input("deseja informar mais alguma nota?")).strip().upper()[0]

        if resp in "SN":
            break
        else:
            print("opcção invalida! tente novamente")
    if resp == "N":
        break

print("dados dos alunos fornecidos:")
print("No :<4 NOME :<10 MEDIA :>8")
for c , i in enumerate(lista):
    print(f"{c:<4}{i[0]:<10}{i[2]}:>8")

while True:
    resp1 =int(input("deseja ver a nota de qual aluno? 999 para sair..."))
    if resp1 == 999:
        print("finalizando o programa...")
    else:
        print(f"nota do aluno {lista[resp1][0]}\n {lista[resp1][1]}")

