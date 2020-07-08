from datetime import date
print("-==-"*20)
print("\033[1;34m ALISTAMENTO MILITAR \033[m")
print("-==-"*20)

nascimento =int(input("informe o seu ano de nascimento:"))

ano = date.today().year

if ano - nascimento > 18:
    print("JA PASSOU DO TEMPO DE SE ALISTAR!")
elif ano - nascimento < 18:
    print("AINDA LHE FALTA ODIO PARA SE ALISTAR!")
else:
    print("ESTA NA HORA DE FAZER SEU ALISTAMENTO!")