matriz = []
linha = 3
coluna = 3



for i in range(linha):
    linha = []
    for j in range(coluna):
        linha.append(i * coluna + j + 1)
    matriz.append(linha)

for linha in matriz:
    print(linha)
  