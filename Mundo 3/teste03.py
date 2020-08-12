def somatorio(a=0,b=0,c=0):
    s = a + b + c
    return s


def funcao():
    n1 = 4
    print(f"n1 dentro vale {n1}")


def somar(a=0,b=0,c=0):
    soma = a + b +c
    print(f"a soma vaale {soma}")


def contador(i,y,x):
    """
    essa funcao tem caracteristica de mostrar o usuario uma forma de contagem dos umeros ate o numero que seja maior ou igual

    """

    print("resultado da funcao")
    while i <= y:
        print(f"{i}")
        i = i + x


print("-"*38)
print("primeiro teste")
print("contador...")
contador(0,10,2)
help(contador)



print("-"*38)
print("segundo teste")
print("somando numeros:")
somar(3,2,5)
somar(3,2)
somar(3)
somar()
print("a proposta e fazer que os valores sejam opcionais")

print("-"*38)
print("terceiro exemplo")
print("-"*38)

n1 = 2
print(f"n1 fora vale {n1}")
funcao()

print("-"*38)
print("quarto exemplo")
print("-"*38)
r1 = somatorio(1,2,3)
r2 = somatorio(3,5)
r3 = somatorio(7)
print(f"os resultadoes foram {r1},{r2} e {r3} ")







