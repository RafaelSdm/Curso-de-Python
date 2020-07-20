num = int(input("informe um numero:"))
print('''Escolha dentre as opcoes a seguir:
[1] conversao em binario
[2] conversão em octal
[3] conversão em hexadecimal''')

escolha = int(input("sua opcao foi:"))

if escolha ==1:
    print("o numero convertido em binario é {}".format(bin(num)[2:]))

elif escolha ==2:
    print("o numero convertido em octal é {}".format(oct(num)[2:]))
elif escolha ==3:
    print("o numero convertido em hexadecimal é {}".format(hex(num)[2:]))
else:
    print("numero invalido!")