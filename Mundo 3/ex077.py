print("achando as vogais das palavras:")

palavras = (str(input("informe uma palavra")).upper(),str(input("informe uma palavra")).upper(),str(input("informe uma palavra")).upper(),str(input("informe uma palavra")).upper(),str(input("informe uma palavra")).upper(),str(input("informe uma palavra")).upper(),str(input("informe uma palavra")).upper(),str(input("informe uma palavra")).upper(),)


for c in palavras:
    print(f"\nna palavra {c} , ela possui as vogais:",end="")

    for lista in c:
        if lista in "AEIOU":
            print(lista,end="")