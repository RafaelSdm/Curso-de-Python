nome =str(input("digite um pequeno texto:")).strip()
maiuscula = nome.upper()
print("a palavra possui {} letras A".format(maiuscula.count("A")))
print("a letrs A aparece na primeira vez na posicao{}".format(maiuscula.find("A")+1))
print("a letra A aparece na ultima vez na posicao{}".format(maiuscula.rfind("A")+1))