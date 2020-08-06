from datetime import date
print("dados do funcionario...")
dicionario = {}

while True:
    dicionario['nome'] = str(input("informe o seu nome:"))
    dicionario['idade'] = (int(input("informe o seu ano de nascimento:")) - date.today().year) *-1
    dicionario['ctps'] = int(input("informe a sua carteira de trabalho: (0 se nao tiver)"))
    if dicionario['ctps'] == 0:
        break
    else:
        dicionario['contrato'] = int(input("Ano de contratação:"))
        dicionario['salario'] = float(input("infrome o seu salario"))
        dicionario['aposentadoria'] = dicionario['contrato'] + 35 - date.today().year + dicionario['idade']
        break

print("analise dos dados do funcionario....")

for i,j in dicionario.items():
    print(f' {i} do funcionário = {j}')




