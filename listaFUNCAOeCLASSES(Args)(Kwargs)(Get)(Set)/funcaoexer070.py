def calculo_salario(horas_trabalhadas,salario_base):
    if horas_trabalhadas <= 40:
        return salario_base
    else:
        valor_por_hora = salario_base / 40
        horas_excedentes = horas_trabalhadas - 40
        valor_hora_extra = (0.5 * valor_por_hora) * horas_excedentes

        return valor_hora_extra + salario_base
    

horatraba = float(input("Digite sua horas trabalhadas:  "))
salariobase = float(input("Digite o seu salario base:  "))

resultado = calculo_salario(horatraba,salariobase)
print(resultado)

    