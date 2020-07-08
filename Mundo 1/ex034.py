salario = float(input("informe seu salario atual:"))

if salario > 2500:
    novoSalario = salario +(salario *(10/100))
    print(" o novo salario sera de R${:.2f}".format(novoSalario))
else:
    novoSalario =  salario + (salario *(15/100))
    print("o novo salario sera de R${:.2f}".format(novoSalario))