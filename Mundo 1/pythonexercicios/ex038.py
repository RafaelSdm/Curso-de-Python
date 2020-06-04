numero1 = int(input("Digite um numero:"))
numero2 = int(input("Informe um segundo numero:"))

if numero1 > numero2:
    print("o numero {} é maior que o numero {}".format(numero1,numero2))
elif numero2 > numero1:
    print("o numero {} é maior que o numero {}".format(numero2,numero1))
else:
    print("o numero {} é igual ao numero {}".format(numero1,numero2))