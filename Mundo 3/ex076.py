print("tabela de preços :")
print("-"*40)
produtos =("celular", 2.50, "oclinho",600,"misto frio",23.67,"pedra amarela azulada",1.60,"pais",78.9,"orquestra",1234.60)
i =1
print("VALOR:")
print("_-"*30)
for c in range(0,12,2):
    print(f"{produtos[c]:.<30}",end="")
    print(f"R${produtos[i]}")
    print()
    i = i +2