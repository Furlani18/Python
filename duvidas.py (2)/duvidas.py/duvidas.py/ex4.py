dicionario = {
    "Star Wars": 1,
    "Vingadores": 1,
    "Deadpool": 2,
    "Homem Formiga": 2,
    "Mulher Maravila": 3,
    "Batman": 3,    
}

Nota_Procurada = int(input("Insira a sua nota: "))
Procurando_chaves_com_nota_procurada = []
for chave in dicionario.keys():
    if Nota_Procurada == dicionario[chave]:
        Procurando_chaves_com_nota_procurada.append(chave)
print(f"Procurando chaves com valor {Nota_Procurada}: ")
print(Procurando_chaves_com_nota_procurada)

