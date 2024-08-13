#Crie um função que imprima a
#quantidade de dígitos de um determinado número
#interio informado.


def contar_digitos(numero):
    numero = abs(numero) # abs() remove qualquer
    if numero == 0:
        print(1)
    else:
        print(len(str(numero)))

# Exemplos de uso
contar_digitos(12345)  # Saída: 5
contar_digitos(-987)   # Saída: 3
contar_digitos(0.9)      # Saída: 1







