matriz = [[2,4,5,6],
          [5,8,9,4],
          [8,9,3,8],
          [9,7,9,9]
          
          
]
linha_maior_soma = None
maior_soma = None

for linha in matriz:
    soma_linha = sum(linha)

    if maior_soma is None or soma_linha > maior_soma:
        maior_soma = soma_linha
        linha_maior_soma = linha


print("A soma da linha é: ",soma_linha)
print("Linha com maior soma: ", linha_maior_soma)



