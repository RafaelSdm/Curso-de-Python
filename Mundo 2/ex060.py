print("CALCULO DE FATORIAL")

fatorial = int(input("Informe um numero do qual iraser fatorado:"))
fat =1
while fatorial >= 1:
    fat = fat * fatorial
    fatorial = fatorial - 1

print("o fatorial de {} é {}".format(fatorial,fat))