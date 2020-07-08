from time import sleep
print("CONTAGEM REGRESSIVA PARA O ANO NOVO!")

numero = int(input("informe de onde ira querer comceçar a contar:"))

for cont in range(numero,0,-1):
    print(cont)
    sleep(1)

print("ano novo garaaiii!!!!")