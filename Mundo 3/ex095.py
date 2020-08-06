print("dados da temporada dos jogadores...")

dados = {}
partadas = []
times =[]

while True:
    dados.clear()
    dados['nome'] = str(input("informe o nome do jogador:"))
    total = int(input(f"quantas partidas o jogador jogou?"))
    partadas.clear()
    for c in range(0,total):
        partadas.append(int(input("informe quantos gols fez na partidaaa:")))
    dados['gols'] = partadas[:]
    dados['total'] = sum(partadas)
    times.append(dados.copy())
    while True:
        resp = str(input("deseja informar mais algum jogador?")).strip().upper()[0]
        if resp in "SN":
            break
        else:
            print("Dados informados invalidos!")

    if resp == "N":
        break
print('=='*30)
print("cod",end="")
for i in dados.keys():
    print(f"{i:<15}",end="")
print()
print('-'*40)
for k,v in enumerate(times):
    print(f"{k:>3} ",end="")
    for d in v.values():
        print(f'{str(d):<15}',end="")
    print()
print("-"*40)

while True:
    quant = int(input("mostrar dados de qual jogador? 999 para sair"))
    if quant == 999:
        break
    if quant > len(times):
        print("nao existe jogador com esse nome")
    else:
        print(f"Dados do jogador {times[quant]['nome']}")
        for i,g in enumerate(times[quant]['gols']):
            print(f"    no jogo {i+1} fez {g} gols")
    print("--"*40)
print("encerrando")