print("VALORES ESCRITOS POR EXTENSO:")

numeros =("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quimze","dezesseis","dezessete","dezoito","dezenove","vinte")

while True:
    valor = int(input("informe um valor de 0 a 20:"))

    if valor >=0 and valor <=20:
        print(f"o numero {valor} escrito por extenso é {numeros[valor]}")
        resp = str(input("deseja informar outro numero?")).strip().upper()[0]
        while True:
            if resp == "S" or resp == "N":
                break
            else:
                print("dados invalidos!")
                resp = str(input("deseja informar outro numero?")).strip().upper()[0]


    else:
        print("valor invalido!")

    if resp == "N":
        break

print("obrigado, volte sempre!")

