def calcular_salario(horas_trabalhadas, salario_base_semanal):
    # Definir carga horária padrão
    carga_horaria_padrao = 40
    
    # Verificar se há horas excedentes
    if horas_trabalhadas > carga_horaria_padrao:
        horas_excedentes = horas_trabalhadas - carga_horaria_padrao
    else:
        horas_excedentes = 0
    
    # Calcular o salário
    salario_normal = salario_base_semanal
    salario_excedente = horas_excedentes * (salario_base_semanal / carga_horaria_padrao) * 0.5
    salario_total = salario_normal + salario_excedente
    
    return salario_total

# Exemplo de uso:
salario_base = 2000.00  # Salário base para 40 horas semanais
horas = 50  # Número de horas trabalhadas na semana

salario = calcular_salario(horas, salario_base)
print(f'O salário a ser pago é: R${salario:.2f}')
