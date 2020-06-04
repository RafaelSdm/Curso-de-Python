print("-==-"*20)
print("\033[0;35;44manalisador de trinagulo \033[m")
print("-==-"*20)
med1 = float(input("digite a medida do primeiro lado:"))
med2 =float(input("digite a medida do segundo lado:"))
med3 = float(input("digite a medida do terceiro lado:"))

if med1 + med2 > med3 and med1 + med3 >med2 and med2 + med3 >med1:
    print("com as medidas dadas acima, é possivel obter um triangulo")
else:
    print("impossivel de obter um triangulo com essas valores")