linha = int(input("Digite a quantidade de linhas: "))
coluna = int(input("Digite a quantidade de colunas: "))

matriz = []

i = 0
while i < linha: ##criar linhas
    lista_linha = []
    j = 0
    while j < coluna: ##preencher as colunas
        lista_linha.append(1)
        j += 1
    matriz.append(lista_linha)
    i = i + 1

x = 0
while x < len(matriz):
    print(matriz[x])
    x = x + 1