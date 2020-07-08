numero = int(input("informe o primeiro numero da PA"))
razao = int(input("informe a razão da PA"))
pa = numero
i =0
n = 10
print(numero)
while i <= n:
    pa = pa + razao
    print("{}".format(pa))
    i = i+1

    if i == 9:
        resp = str(input("deseja obervar mais razoes?[S/N]")).upper()

        if resp == 'S':
            n = int(input("informe quantas vezes queira prosseguir..."))
            n = n + i

            while i < n:
                pa = pa + razao
                print("{}".format(pa))
                i = i+1
        else:
            i = i+1