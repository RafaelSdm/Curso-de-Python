print("-==-"*20)
print("CALCULO DO IMC:")
print("-==-"*20)

peso = float(input("Informe seu peso:"))
altura = float(input("informe sua altura:"))

imc = peso / (altura * altura)

print("SEU IMC ESTA EM {:.2f}".format(imc))

if imc <= 18.5:
    print("VOCE ESTA ABAIXO DO PESO:")
elif imc >= 18.6 and imc <= 25:
    print("PARABENS! VOCE ESTA NO PESO IDEAL")
elif imc >= 25.1 and imc <= 30:
    print("VOCE ESTA EM SOBREPESO")
elif imc >= 30.1 and imc <=40:
    print("VOCE ESTA EM GRAU DE OBESIDADE")
else:
    print("OBESIDADE MORBIDA!")