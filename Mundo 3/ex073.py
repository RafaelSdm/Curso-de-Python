print("tabela do campeonato brasileiro:")
print("-"*20)
times = ("palmeiras","flamengo","internacional","gremio","sao paulo","atletico minneiro","atletico paranaense","cruzeiro","botafogo","santos","bahia","fluminense","corinthians","chapecoense","ceara","vasco","sport","america","vitoria","parana")
pos = 0

for c in range(0, len(times)):
     print(f"{c +1}- {times[c]}")
print("-"*20)

print("os times classificados para a libertadores:")
print("+"*20)

for c in range(0,5):
    print(f"{c +1} - {times[c]}")
print("+"*20)


while True:
    if times[pos] == "chapecoense":
        posicao = pos
        print("o time da chepecoense esta na {} posiçao".format(pos +1))
        break
    else:
        pos = pos +1

print("times que foram rebaixados:")
print(f"{times[-4:]}")

print("-"*20)
print("colocando os times em ordem alfabetica:")
print()


alfabetico = sorted(times)
for c in range(0, len(times)):
    print(f"{c+1} - {alfabetico[c]}")
print("*"*20)