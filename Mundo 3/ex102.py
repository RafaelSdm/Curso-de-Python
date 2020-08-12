def linhas():
    print("-"*30)


def fat(x,b=0):
    f =1
    if b ==0:


        for c in range(x,1,-1):

            f = f * c

        print(f"o resultado é {f}")
    else:
        for c in range(x,1,-1):
            print(f" {c} x",end='')
            f = f*c

        print(f" 1 = {f}",end='')



linhas()
print("calculo de fatorial")
linhas()

fatorial = int(input("informe o numero que ira ser fatorado!"))
r = str(input("deseja se que apareca o processo da conta?")).upper().strip()[0]
if r == "S":
    fat(fatorial,r)
else:
    fat(fatorial)
