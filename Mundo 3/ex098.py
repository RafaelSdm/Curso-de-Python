from time import sleep
def lista():
    print("-"*30)
def cont(x,y,i,j):


    if j ==1:
        while i <=10:
            print(f' {i} ',end='')
            sleep(0.5)
            i = i+1

        print()
    elif j == 2:
        while x >= y:
            print(f" {x} ",end="")
            sleep(0.5)
            x = x-i
        print()
    elif j ==3:
        if x < y:
            while x <=y:
                print(f' {x} ',end='')
                sleep(0.5)
                if i >0:
                    x = x+i
                elif x <0:
                    x = x -i
                elif x ==0:
                    x = x+1
            print()
        else:
            while x >= y:
                print(f" {x} ",end="")
                sleep(0.5)
                if i >0:
                    x = x -i
                elif i < 0:
                    x = x +i
                elif i ==0:
                    x = x+1




lista()
print("contagem dos numeros...")
lista()

lista()
print("contagem feita de 1 a 10...")
cont(0,0,0,1)

lista()
print("contagem feita de 10 a 0 pulando em 2 a 2")
cont(10,0,2,2)

lista()
print("contagem proposta pelo usuário...")
a = int(input("informe o numero de inicio:"))
b = int(input("informe o numero final"))
c = int(input("informe o passe:"))
print(f"contagem de {a} ate {b} pulando de {c} em {c}...")
lista()
sleep(0.3)
cont(a,b,c,3)
