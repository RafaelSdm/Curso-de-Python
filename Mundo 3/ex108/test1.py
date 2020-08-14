from ex108 import moeda
dinheiro = float(input("informe o dinheiro"))
print(f"o dobro de {moeda.moeda(dinheiro)} é {moeda.moeda(moeda.dobro(dinheiro))}")
print(f"a metade de {moeda.moeda(dinheiro)} é {moeda.moeda(moeda.metade(dinheiro))}")
print(f"aumentando 10% de {moeda.moeda(dinheiro)} temos R${moeda.moeda(moeda.porcentagem(dinheiro))}")
print(f"reduzindo 13% de {moeda.moeda(dinheiro)} temos {moeda.moeda(moeda.reduzindo(dinheiro))}")