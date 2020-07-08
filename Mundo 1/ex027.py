nome =str(input("digite seu nome completo:"))
separa = nome.split()
print("o primeiro nome é {}".format(separa[0]))
print("o ultimo nome de fulano é {}".format(separa[len(separa)-1]))