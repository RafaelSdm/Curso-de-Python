print("analise estatistico de grupos")
somaid =0
feminino =0
masculino =0
while True:
    print("_"*20)
    idade = int(input("Informe sua idade:"))
    sexo = str(input("informe seu sexo:[M/F]")).upper()
    print("-"*20)

    if idade >= 18:
        somaid = somaid + 1

    if sexo == "M":
        masculino = masculino +1
    elif sexo != "F":
        print("opcao invalida!")

    if idade >=20 and sexo =='F':
        feminino = feminino +1


    while True:
        resp = str(input("deseja informar novamente?")).upper()

        if resp ==  'S' or resp == 'N':
            break
        elif resp != 'N' and resp != 'S':
            print("opcao invalida")
    if resp == 'N':
        break
print("="*10)
print(f"Dados impressos:\n{somaid} maiores de idade \n{masculino} do sexo masculino no gruupo\n{feminino} mulheres com 20 anos ou mais")
print("="*10)
