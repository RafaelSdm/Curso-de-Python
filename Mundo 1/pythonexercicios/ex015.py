dia =int(input("quantos dias alugou o carro:"))
km =float(input("qunatos quilometros andou:"))

preco = (dia* 60) + (km * 0.15)

print("o preço do aluguel ficou em R${}".format(preco))