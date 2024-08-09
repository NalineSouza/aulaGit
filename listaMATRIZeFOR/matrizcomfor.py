linha = int(input("Digite a quantidade de linhas: "))
coluna = int(input("Digite a quantidade de colunas: "))
matrix = []

for i in range(linha):
    linha = []
    for j in range(coluna):
        num = int(input("Digite um numero: "))
        linha.append(num)
        matrix.append(linha)

for item in matrix:
    print(item)