matriz = [[10,15,20],[25,30,35],[40,45,50]]
matriz_nova = []

for linha in matriz:
    linha_nova = []
    for item in linha:
        linha_nova.append(item * 5)
    matriz_nova.append(linha_nova)


print(matriz[0])
print(matriz[1])
print(matriz[2])

print()

print(matriz_nova[0])
print(matriz_nova[1])
print(matriz_nova[2])
