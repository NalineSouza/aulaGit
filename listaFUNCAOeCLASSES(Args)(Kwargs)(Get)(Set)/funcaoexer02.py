## Crie uma função para calcular a exponenciação, que necessite dois argumentos e apresente como resultado a potência. 
#Sendo base elevado ao expoente.



####EXEMPLO 001
def calcular_exponenciacao(base,expo):
    x = base ** expo
    return x

a = calcular_exponenciacao(4,8)

print(a)
####EXEMPLO 002
def digitos(numero):
    numero1 = str(numero)
    digitos = len(numero1)
    return digitos


digitos1 = int(input("Digite um numero: "))
print(digitos(digitos1))
