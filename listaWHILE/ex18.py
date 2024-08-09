quantidadenumero = int(input("Quantos numeros voce gostaria de de ler:  "))
valores = []
cont = 0

while cont < quantidadenumero:
    valor = int(input("Digite o numero: "))
    valores.append(valor)
    cont = cont + 1

print(max(valores))

