
def calcular_consumo(potencia,tempo):
    return (potencia / 1000) * tempo

def calcular_conta(consumo, valor_kWh):
    return consumo * valor_kWh

potencia = 1500  
tempo = 5        
valor_kWh = 0.80 

consumo = calcular_consumo(potencia, tempo)
print(f"Consumo: {consumo:.2f} kWh")

custo = calcular_conta(consumo, valor_kWh)
print(f"Custo: R${custo:.2f}")