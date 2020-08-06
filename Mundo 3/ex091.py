from random import randint
from time import sleep
print("jogos dos dados:")
dados = {}
cont = 1
posicao =0

dados['jogador1'] = randint(1,6)
dados['jogador2'] = randint(1,6)
dados['jogador3'] = randint(1,6)
dados['jogador4'] = randint(1,6)
print("Enviando os numeros para cada jogador...")

for i, j in dados.items():
    print(f"o {i} tirou o {j}")
    sleep(1.3)
print('-'*50)
print("o venceder foi aquele que tirou o maior numero...")
print("lista na ordem de suas posicoes")
print('-'*50)
for i in sorted(dados, key=dados.get ,reverse=True):
    print(f"o {i} tirou o {dados[i]} e ficou na {posicao+1}° colocação" )
    sleep(0.8)
    posicao = posicao +1
    if cont == 1:
        vencedor = i
        cont = cont +1
print("="*50)
print(f"parabens {vencedor}!!! VOCE VENCEUU")
print("="*50)



