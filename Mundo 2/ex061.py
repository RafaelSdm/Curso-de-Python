print("progressao aritimetica")

numero = int(input("informe o primeiro numero da P.A"))
razao = int(input("informe agora sua razão:"))
pa = numero

i =0

while i < 10:
    pa = pa + razao
    print("[{}]".format(pa),end='')
    i = i +1