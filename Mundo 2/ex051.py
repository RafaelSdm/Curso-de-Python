print("construçao de uma progressão aritimética")

numero = int(input("informe o primeiro numero da P.A:"))
razao = int(input("informe agora a razão dessa P.A:"))

dez = numero + (10 -1) * razao

for c in range(numero, dez + razao, razao):
    print("{}".format(c))
