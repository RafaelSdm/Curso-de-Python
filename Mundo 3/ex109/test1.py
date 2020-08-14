from ex109 import moeda
dinheiro = float(input("informe o dinheiro"))
print(f"o dobro de {moeda.moeda(dinheiro)} é {moeda.dobro(dinheiro,True)}")
print(f"a metade de {moeda.moeda(dinheiro)} é {moeda.metade(dinheiro,True)}")
print(f"aumentando 10% de {moeda.moeda(dinheiro)} temos R${moeda.porcentagem(dinheiro,True)}")
print(f"reduzindo 13% de {moeda.moeda(dinheiro)} temos {moeda.reduzindo(dinheiro, True)}")