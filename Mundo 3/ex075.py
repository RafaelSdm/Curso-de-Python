print("dados da tupla:")
numeros  = (int(input("informe um numero:")),int(input("informe outro numero:")),int(input("informe um numero:")),int(input("informe um numero")))
cont9 =0
guarda =-1
print("valores informados:")
for c in range(0,4):
    print(f" {numeros[c]} ",end="")
print()
print("analise dos numeros:")

for c in range(0,4):
    if numeros[c] == 9:
        cont9 = cont9 +1
    if numeros[c] == 3:
        guarda = c
print(f"o numero 9 aparceu {cont9} vezes ")

if guarda !=-1:
    print(f"o numero 3 apareceu primeiramente na posicao {guarda+1}")
else:
    print("o numero 3 nao apareceu")
print("lista dos numeros pares:",end="")
for c in range(0,4):
    if numeros[c] %2 ==0:
        print(f" {numeros[c]} ",end="")



