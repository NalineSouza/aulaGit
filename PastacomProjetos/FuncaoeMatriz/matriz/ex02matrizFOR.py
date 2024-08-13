matriz = []
lin = 4
col = 4

for i in range(lin):
    linha = []
    for j in range(col):
        num = int(input(f"Digite um valor para a coluna{j + 1}: "))
        linha.append(num)

    matriz.append(linha)

for linha in matriz:
    print(linha)

    