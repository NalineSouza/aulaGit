def consumo_luz(potencia_eletrica,tempo_ligado):
    resultado = tempo_ligado * potencia_eletrica
    return resultado


def calcular_conta_energia(consumo,valorkwh):
    return consumo * valorkwh

tempoligado = float(input("Digite o tempo em que o aparelho ficou ligado: "))
potenciaeletrica = float(input("Digite  a potencia por hora:  "))

res = consumo_luz(tempoligado,potenciaeletrica)
ress = calcular_conta_energia()
