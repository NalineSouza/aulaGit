salario_carlos = float(input("Digite o valor do salario de Carlos:  "))
salario_joao = salario_carlos / 3

print(f"Salario de Joao: {salario_joao}")
print(f"Salario de Carlos: {salario_carlos}")

mes = 0
while(salario_joao <= salario_carlos):
    rendimentosMesjoao = salario_joao * 0.05
    rendimentosMescarlos = salario_carlos * 0.02

    salario_joao = salario_joao + rendimentosMesjoao
    salario_carlos = salario_carlos + rendimentosMescarlos

    mes += 1

print(f"Salario do carlos em {mes} meses: {salario_carlos:.2f}")
print(f"Salario do joao em {mes} meses: {salario_joao:.2f}")

print(f"Em {mes} meses o joao terá em salario maior que o de carlos.")