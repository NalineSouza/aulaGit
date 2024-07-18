import random

numero_aleatorio = random.randint(1, 100)

numero_digitado = int(input("Tente adivinhar o numero gerado: "))

tentativa = 1

while(numero_digitado != numero_aleatorio):
    tentativa = tentativa + 1

    if(numero_digitado > numero_aleatorio):
        print("O numero digitado é maior do que o numero gerado:")


    else:
        print("O numero é menor do que o numero gerado!")


    numero_digitado = int(input("Tente adivinhar o numero gerado: "))

print(f"Voce acertou o numero gerado na tentativa {tentativa}!!")
