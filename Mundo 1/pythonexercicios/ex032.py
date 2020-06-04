from datetime import date
ano = int(input("qual ano voce quer saber se vai ser bissexto:?"))
if ano ==0:
    ano = date.today().year

if ano %4 == 0 and ano %100 != 0 or ano %400 == 0:
    print("o ano {} sera ou foi um ano bissexto".format(ano))
else:
    print(" o ano {} nao sera ou foi um ano bissexto".format(ano))