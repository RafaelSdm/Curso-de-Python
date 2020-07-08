distancia = float(input("a sua viagem sera de quantos kilometros?:"))

if distancia <= 200:
    valor = distancia * 0.50
    print("a distancia da viagem é de {:.2f}KM e o valor da passagem é de R${:.2f}".format(distancia,valor))
else:
    valor = distancia * 0.45
    print("a distancia da viagem é de {:.2f}KM e o valor da passagem é de R${:.2f}".format(distancia,valor))