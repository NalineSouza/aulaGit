horatrabalhada = float(input("Digite suas horas trabalhadas: "))
salario = horatrabalhada * 40.50

if salario > 2500:
    imposto = 0.11 * salario
    print(f"Seu salario atualmente é {imposto}")
    

else:
    print(f"Seu salario é {salario} ")

