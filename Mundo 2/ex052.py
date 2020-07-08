numero = int(input("informe um numero do qual voce queira saber se é primo:"))
x = 0
for c in range(1,numero+1):
        if numero / c ==0:
            x = x + 1

if x > 2:
    print("o numero {} nao é primo")
else:
    print("o numero é primo")
