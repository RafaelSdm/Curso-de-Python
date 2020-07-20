a = float(input("informe a medida de A"))
b = float(input("informe a medida de B"))
c = float(input("informe a medida de C"))

if a + b > c and a + c > b and c + b > a:
    print("dadas essas medidas é possivel ter um triangulo")
    if a == b == c:
        print("temos um triangulo equilatero")
    if a != b != c !=a:
        print("temos um triangulo escaleno")
    else:
        print("temos um triangulo isosceles")

else:
    print("impossivel ter um trinagulo com essas medidas")

