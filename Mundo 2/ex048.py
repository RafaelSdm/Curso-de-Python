print("soma dos numeros ímpares e multiplos de 3 entre 1 a 500:")

s =0

for c in range(1,501):
    if c %2 != 0:
        print("{}".format(c),end= " ")
        if c %3 ==0:
            s = s + c

print("a soma dos numeros multiplos de 3 são de {}".format(s))