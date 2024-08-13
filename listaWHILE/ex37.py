    # Solicita ao usuário para digitar um número
numero = int(input("Digite um número: "))

# Verifica se o número é primo
if numero <= 1:
    primo = False
else:
    primo = True
    i = 2
    while i <= numero ** 0.5:
        if numero % i == 0:
            primo = False
            break
        i += 1

# Exibe o resultado
if primo:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
