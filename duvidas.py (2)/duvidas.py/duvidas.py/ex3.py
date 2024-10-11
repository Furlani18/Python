L = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input("Digite um numero: ")))
    L.append(linha)
Soma = 0
for i in range(len(L)):
    for j in range(len(L[i])):
        # print(L[i][j], end=" ") 
        if i == j:
            Soma=Soma+L[i][j]
print(f"Soma da diagonal:{Soma} ")