print("_=_=+"*20)
print("calculo com a flag(break)")
print("-+--_="*20)
numero = 0
i =0
soma =0
while True:
    numero = int(input("Informe um numero ou 999 para sair:"))

    if numero == 999:
        break
    else:
        soma = soma + numero
        i = i+1

print(f"a soma dos {i} valores calculados é de {soma}")