import random
nome = input("nome do aluno:")
nome2 = input("nome do aluno:")
nome3 = input("nome do aluno")
nome4 = input("nome do aluno:")

escolhido = random.choice([nome,nome2,nome3,nome4])
print("o aluno escolhido pela professora foi o(a),{}".format(escolhido))