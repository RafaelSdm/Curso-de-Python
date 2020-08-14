def linhas():
    print("_"*30)

def analise(x ='desconhecido', y =0):
   print(f"o jogaodor {x},fez {y} gols na temporada ")



linhas()
print("analise do jogaor")
linhas()
nome = str(input("informe o nome do jogador:"))

gols = str(input("informe quantos gols fez:"))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == "":
    analise(y = gols)
else:
    analise(nome,gols)