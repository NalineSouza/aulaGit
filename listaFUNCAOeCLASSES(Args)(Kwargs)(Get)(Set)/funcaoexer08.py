def calcula_excedente(quantidade_kilo_peixes):
    if quantidade_kilo_peixes > 50:
        peso_excedente = quantidade_kilo_peixes - 50
        valor_excedente = peso_excedente  * 4
        valor_multa = valor_excedente
        return valor_multa
    



res = float(input("Digite a quantidade de kilos que voce pescou:  "))
resultado = calcula_excedente(res)
print(f"Sua multa por ter pescado acima do limite de 50 kilos é {resultado} reais!!")


