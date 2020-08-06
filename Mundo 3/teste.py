pessoas = {'nomes': "Rafael","sexo":"macho alfa","idade":19}
print(f"o {pessoas['nomes']} que se considera um  {pessoas['sexo']} possui {pessoas['idade']}")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for c in pessoas.keys():
    print(c)

for c in pessoas.values():
    print(c)
for c, j in pessoas.items():
    print(f"o {c} pertence ao {j}")

del pessoas['sexo']
print(pessoas)

pessoas["sexo"] = "macho alfa"

print(pessoas)

print("outro codida daqui pra frente \n\n\n\n\n\n")
estado1 = {'estado': 'minas gerais', 'cidade':'capela nova' }
estado2 = {'estado':'rio de janeiro', 'cidade':"rossinha"}

brasil = []

brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(f"o brasil possui um estado chamado {brasil[0]['estado']} e a prorpia possui uma cidade chamada {brasil[0]['cidade']}")


print("-"*45)

es = {}
br = []

for c in range(0,3):
    es['estado'] = str(input("informe o seu estado:"))
    es['cidade'] = str(input("informe a sua cidade:"))
    br.append(es.copy())

for c in br:
    for i,j in c.items():
        print(f"o campo {i} tem valor {j}")
