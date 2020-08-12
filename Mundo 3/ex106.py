def linhas():
    print("-"*45)

linhas()
print("significados das funco~es em  python")
linhas()

while True:
    resp = str(input("informe qual funcao queira saber:"))

    help(resp)

    while True:


        r = str(input("deseja informar novemnte?")).upper().strip()[0]

        if r in "SN":
            break
        else:
            print("dados invalidos!")
    if r == "N":
        break


