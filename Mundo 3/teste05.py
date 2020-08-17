try:
    n = int(input("informe um numero:"))
    m = int(input("informe o denominador"))
    r = n/m
except (ValueError, TypeError):
    print('tivemos problema com o tipo de dado que voce enviou')
except KeyboardInterrupt:
    print('nao é possivel dividir um numero por zero')
except ZeroDivisionError:
    print('nao da pra dividir por zero')

else:
    print(f"o resultado é {r}")
finally:
    print("volte sempre valeu falou")