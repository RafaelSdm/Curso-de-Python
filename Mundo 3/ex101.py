from datetime import date
def linhas():
    print("+="*20)

def analise(x):
    if x < 16:
        resp = "voto negado"
        return resp
    elif x >= 16 and x <18:
        resp = "voto opcional"
        return resp
    else:
        resp = "voto obrigatorio"
        return resp

linhas()
print("analise dos votos:")
linhas()

ano = int(input("informe o ano que voce nasceu:"))
idade = date.today().year - ano
print(f"voce nasceu em {ano} e tem {idade} anos")
print(f"nesse caso, voce esta na faixa etaria do {analise(idade)}")


