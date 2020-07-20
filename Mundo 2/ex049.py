from time import sleep
print("TABUADA:")
numero = int(input("Informe um numerp pelo qual irá ser multiplicado:"))

print("gerando a tabuada:")

for c in range(0,11):
    print("{} X {} = {}".format(numero,c,numero*c))
    sleep(0.5)