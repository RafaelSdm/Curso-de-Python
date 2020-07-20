altura =float(input("altura da parede:"))
largura = float(input("largura:"))

area = float(largura*altura)

tinta = float(area/2)

print("a area é {:.2f} e gasta {:.2f} litrso de tinta".format(area,tinta))