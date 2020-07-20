from datetime import date
print("-==-"*20)
print("\033[1;34m ALISTAMENTO MILITAR \033[m")
print("-==-"*20)

nascimento =int(input("informe o seu ano de nascimento:"))
genero = str(input("informe o seu sexo:")).upper()

ano = date.today().year

if genero == "FEMININO":
    if ano - nascimento > 20:
        print("PRECISA SE ALISTAR IMEDIATAMENTE!")
    elif ano - nascimento < 20:
        print("VOCE AINDA NAO POSSUI A IDADE MINIMA PARA SE ALISTAR!")
    else:
        print("VA SE ALISTAR AGORA!")

elif genero == "MASCULINO":
    if ano - nascimento > 18:
        print("JA PASSOU DO TEMPO DE SE ALISTAR!")
    elif ano - nascimento < 18:
        print("AINDA LHE FALTA ODIO PARA SE ALISTAR!")
    else:
        print("ESTA NA HORA DE FAZER SEU ALISTAMENTO!")

else:
    print("genero indefinido! Tente novamente!")