def linhas():
    print("-=_-="*20)
def calculo(x,y):
    area = x * y
    linhas()
    print(f"A proporção de {x} x {y} promove uma area de {area:.2f} metros quadrados ")

linhas()
print("Calculo da area do terreno:")
linhas()

comprimento = float(input("informe o comprimento da area:"))
largura = float(input("informe a largura da area calculada:"))

calculo(comprimento,largura)
