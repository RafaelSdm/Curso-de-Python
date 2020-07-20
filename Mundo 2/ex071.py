print("cedulas do caixa:")

valor = int(input("informe o valor a ser sacado:"))
resto =0
nota20 =0
nota50 = valor // 50
nota10 =0
nota1 =0

if nota50 > 0:
    print(f"as cedulas de irao vir com o total de {nota50} notas")
    resto = nota50

if resto == 0:
    nota20 = nota20 // 20

    if nota20 > 0:
        print(f"o total de cedulas de 20 reais é de {nota20}")
        resto = nota20
else:
    nota20 = resto // 20
    if nota20 > 0:
        print(f"o valor total de cedulas de 20 reais é de {nota20}")
        resto = nota20

if resto == 0:
    nota10 = nota10 // 10

    if nota10 > 0:
        print(f"o total de cedulas de 10 reais é de {nota10}")
else:
    nota10 = resto //10

    if nota10 > 0:
        print(f"o valor de cedulas de 10 reais é de {nota10}")

if resto == 0:
    nota1 = nota1 //1

    if nota1 > 0:
        print(f"o valor de cedulas de 1 real é de {nota1}")
else:
    nota1 = resto //1

    if nota1 > 0:
        print(f"o valor de cedulas de 1 real é de {nota1}")