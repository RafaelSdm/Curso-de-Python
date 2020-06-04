preco = float(input("informe o preço do produto:"))
desc = float( preco*(5/100))

print("o desconto d produto ira custar R${:.2f}".format(preco - desc))