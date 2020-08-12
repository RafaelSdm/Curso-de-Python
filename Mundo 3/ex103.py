def linhas():
    print("_"*30)

def analise(x =0, y =0):
    if x ==0:
        n1 = 'desconhecido'
    else:
        n1 = x
    print(n1)



linhas()
print("analise do jogaor")
linhas()
nome = str(input("informe o nome do jogador:"))

gols = str(input("informe quantos gols fez:"))

analise(nome,gols)