palavra = str(input("digite uma frase ou um pequeno texto:")).strip().upper()
frase = palavra.split()
junto =''.join(frase)
inverter = ''

for letra in range(len(junto)-1,-1,-1):
    inverter += junto[letra]
if inverter == junto:
    print("a frase é polindreta")
else:
    print("essa frase nao é polimdreta")