print("validação masculina/ feminina")

resp = 1

while resp ==1:
    sexo = str(input("informe o se sexo: [F/M]")).upper()

    if sexo == 'F' or sexo == 'M':
        resp = resp +1
    else:
        print("os dados informados estão incorretos, digite novamente:")

if sexo == "F":
    print("tenha um bom dia senhora!")
else:
    print("tenha um bom dia senhor!")