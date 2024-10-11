import random
A = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(random.randint(0, 99))
    A.append(linha)
print("A Matriz Completa")

for i in range(len(A)):
    for j in range(len(A[i])):
        print("%4d" % A[i][j], end=" ")
    print()

print("A Primeira Coluna: ")
for i in range(10):
    print(A[i][0])