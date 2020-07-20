print("-==-"*20)
print("\033[1;31m analisador de emprestimos:\033[m")
print('-==-'*20)

preco = float(input("qual é o preço da casa que queira comprar?"))
salario =float(input("informe o seu salario:"))
anos = int(input("em quantos anos voce pensa em pagar a casa?"))

permissao = salario*(30/100)
parcelas = preco / (12 * anos)

if permissao >= parcelas:
    print("\033[1;32m SUA CONDIÇÃO PARA O EMPRESTIMO FOI CONCEDIDA!PARABENS!\033[m")
else:
    print("\033[1;31m PEDIDO NEGADO, SEU SALARIO INFELIZMENTE NAO BATE COM OS PEDIDIOS!\033[m")

