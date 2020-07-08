km = int(input("qual era a sua velocidade:"))

if km > 80:
    m = km - 80
    multa = m*7

    print("voce ira pagar em multa em um total de R${:.2f}".format(multa))
else:
    print("voce é um bom motorista, seu lugar ta guardado")
