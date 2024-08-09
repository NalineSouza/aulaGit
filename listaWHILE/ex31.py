salario = 4000
ano = 2021
aumento = 0.015

while ano <= 2024:
    salario += (salario * aumento)
    print(f"PERCENTUAL DE AUMENTO {aumento} no {ano}")
    print(f"SALARIO no {ano} R$ {salario}")
    aumento = aumento * 2
    ano = ano + 1

print(salario)