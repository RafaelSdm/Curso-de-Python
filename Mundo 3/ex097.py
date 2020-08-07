from time import sleep


def linhas():
    print("_-_"*15)
def tam(a):
    print("-"*a,end="" )
    print("-"*4)
    print(f"  {mensagem}")
    print("-"*a,end='')
    print("-"*4)
    print()



linhas()
print("Linhas adaptativas com a mensagem")
linhas()

mensagem = str(input("informe uma palavra ou um pequeno texto...")).strip()
tamanho = len(mensagem)

print(f"o tamanho da {mensagem} é de {tamanho}")
linhas()
print("analisando o formato da linha...")
sleep(2)

tam(tamanho)