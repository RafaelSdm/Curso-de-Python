preco = float(input("informe o preço do produto:"))

print("MANEIRAS DE PAGAMENTO:")
print("OPÇÃO 1 = A VISTA")
print("OPÇÃO 2 = A VISTA NO CARTÃO")
print("OPÇÃO 3 = 2X NO CARTÃO")
print("OPÇÃO 4 = 3X NO CARTÃO")

forma =str(input("DIGITE SUA FORMA DE PAGAMENTO:"))

if forma == "A VISTA":
    gasto = preco - (preco*(10/100))
    print("VOCE IRA PAGAR R${:.2f}".format(gasto))
elif forma == "A VISTA NO CARTÃO":
    gasto = preco - (preco*(5/100))
    print("VOCE IRA PAGAR R${:2.f}".format(gasto))
elif forma == "2X NO CARTÃO":
    gasto = preco
    print("VOCE IRA PAGAR R${:.2f}".format(gasto))
elif forma == "3X NO CARTÃO":
    gasto = preco + (preco*(20/100))
    print("VOCE IRA PAGAR R${:.2f}".format(gasto))
else:
    print("DADOS INVALIDOS!")