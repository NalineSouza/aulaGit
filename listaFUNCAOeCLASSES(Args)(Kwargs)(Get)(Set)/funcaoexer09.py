def calcular_tempo(tempo_em_minutos=int):
    if tempo_em_minutos > 60:
        minutos_passados = tempo_em_minutos - 60
        horas_adicionais = int(minutos_passados / 60)
        if horas_adicionais <= 0:
            return 9 + 1.50
        valor = 9 + 1.50 + (horas_adicionais * 1.50)
        return valor
    
    elif tempo_em_minutos < 15:
        return 0
    else:
        return 9
        

resultado = int(input("Digite as minutos que voce ficou estacionado:  "))
res = calcular_tempo(resultado)

print(res)