import random
A = []
for i in range(10):
    linha = []
    for j in range(15):
        linha.append(random.randint(0, 9))
    A.append(linha)
print("Matriz Completa: ")

for i in range(len(A)):
    for j in range(len(A[i])):
        print("%4d" % A[i][j], end=" ")
    print()
print("Primeira Coluna: ")
for i in range(10):
    print(A[i][0])



