import random
aluno1 = input("nome do aluno:")
aluno2 = input("nome do aluno:")
aluno3 = input("nome do aluno:")
aluno4 = input("nome do aluno:")

seq = random.sample([aluno1,aluno2,aluno3,aluno4],4)
print("a ordem de quem irá aprensentar os trabalhos:")
print(seq)