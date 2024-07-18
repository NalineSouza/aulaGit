num_a = int(input("Digite um numero: "))
num_b = int(input("Digite outro numero: "))
cont = 0

while(num_a <= num_b):
    primo = True
    i = 2
    while i <= num_a ** 0.5:
         if num_a % i == 0:
            primo = False
            break
         i += 1
    if(primo):
        print(f"É primo: {num_a}")
        cont += 1

    num_a += 1

print(f" Existem {cont} numeros primos entre {num_a} e {num_b}")