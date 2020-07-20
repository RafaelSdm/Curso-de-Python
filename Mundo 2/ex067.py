import time
print("tabuada")

while True:
    numero = int(input("informe o numero que deseja efetuar a sua tabuada:"))
    print()
    if numero >=0:
        print("_=+_"*12)
    if numero >=0:
        for cont in range(1,11):
            print(f"{numero} x {cont} = {numero*cont}")
            time.sleep(0.3)
        print("_=+_"*12)
    else:
        break
print("VOLTE SEMPRE:)")