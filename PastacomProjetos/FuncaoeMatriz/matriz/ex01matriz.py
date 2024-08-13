matriz = []

contador = 1
i = 0
while i < 3:
    linha = []
    j = 0

    while j < 3:
        linha.append(contador)
        contador += 1
        j += 1

    matriz.append(linha)
    i += 1

    x = 0
    
while x < len(matriz):
    print(matriz[x])
    x = x + 1
   
