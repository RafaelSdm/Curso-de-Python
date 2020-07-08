print("soma dos numeros pares:")

s =0

for c in range(0,6):
    num = int(input("Informe o {}° numero:".format(c+1)))

    if num %2 ==0:
        s = s + num

print("a soma dos numeros pares são = {}".format(s))