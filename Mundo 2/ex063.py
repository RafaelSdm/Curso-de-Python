print("sequencia de fibonacci!")

sequencia = int(input("informe quantas vezes a sequncia ira aparecer:"))
c = 0
soma =0

while c <= sequencia:
    if c == 0:
        print("{} ->".format(c),end=" ")
        c = c+1
    elif c == 1:
        print("{} ->".format(c),end="")
        c = c+1
    elif c == 2:
        soma = 1
        print("{} ->".format(soma),end="")
        soma =0
        c = c+1
    else:
        soma = soma + c
        print("{} ->".format(soma),end="")
        c = c+1
