print("analise da temporada do jogador de futebol...")

dados = {}
partidas = []
total =0

dados['nome'] = str(input("informe o nome do jogador:"))
part = int(input(f"quantas partidas {dados['nome']} jogou?"))

for c in range(0,part):
    partidas.append(int(input(f"quantos gols {dados['nome']} fez na {c+1}° partida? ")))

for c in range(0,part):
    total = total + partidas[c]

dados['gols'] = partidas[:]
dados['total'] = total

#print(f"{dados['nome']} fez {total} gols")
print("=-"*30)
print(dados)
print("-="*30)
print("-="*30)
for c,x in dados.items():
    print(f"a chave {c} tem o valor de {x}")
print("-="*30)
print("-="*30)

for c,x in enumerate(dados['gols']):
    print(f"na {c+1}° partida, {dados['nome']} marcou {x} gols")
print("-="*30)

print(f"no final da temporada, {dados['nome']}  marcou {total} gols ")