print("matriz 3x3")

matriz = [[0,0,0],[0,0,0],[0,0,0]]
par =0
soma3 =0
maior =0
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f"informe o numero da linha {i+1} e coluna {j+1} da matriz"))

print("resultado da matriz:")

for c in range(0,3):
    for i in range(0,3):
        print(f"[{matriz[c][i]:^5}]",end="")
    print()

print("dados da matriz:")

for c in range(0,3):
    for i in range(0,3):
        if matriz[c][i] %2 ==0:
            par = par + matriz[c][i]
print(f"a soma dos numeros pares da matriz é de {par}")

for c in range(0,3):
    for i in range(0,3):
        if c == 2:
            soma3 = soma3 + matriz[c][i]

print(f"a soma dos numeros da terceira coluna é de {soma3}")
maior = matriz[1][0]
for c in range(0,3):
    for i in range(0,3):
        if c == 1:
            if matriz[c][i] > maior:
                maior = matriz[c][i]

print(f"o maior valor da segunda coluna é de {maior}")



