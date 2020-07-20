preco = float(input("informe o preço do produto:"))

print("MANEIRAS DE PAGAMENTO:")
print("OPÇÃO 1 = A VISTA")
print("OPÇÃO 2 = A VISTA NO CARTÃO")
print("OPÇÃO 3 = 2X NO CARTÃO")
print("OPÇÃO 4 = 3X OU MAIS NO CARTÃO")

forma =int(input("DIGITE SUA FORMA DE PAGAMENTO:"))

if forma == 1:
    gasto = preco - (preco*(10/100))
elif forma == 2:
    gasto = preco - (preco*(5/100))
elif forma == 3:
    gasto = preco
elif forma == 4:
    gasto = preco + (preco*(20/100))
    parcelas = int(input("EM QUANTAS VEZES DESEJA PAGAR ESSA CONTA?"))
    divido = preco/ parcelas
    print("A sua conta ira sair em {}x de R${:.2f}".format(parcelas,divido))
else:
    print("DADOS INVALIDOS!")
print("voce acaba de efetuar uma compra de R${:.2f} e vai te custar R${:.2f}".format(preco, gasto))
print("SO AGRADECE!")

