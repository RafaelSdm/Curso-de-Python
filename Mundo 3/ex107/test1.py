from ex107 import moeda
dinheiro = float(input("informe o dinheiro"))
print(f"o dobro de R${dinheiro} é {moeda.dobro(dinheiro)}")
print(f"a metade de R${dinheiro} é {moeda.metade(dinheiro)}")
print(f"aumentando 10% de R${dinheiro} temos R${moeda.porcentagem(dinheiro)}")
print(f"reduzindo 13% de R${dinheiro} temos {moeda.reduzindo(dinheiro)}")