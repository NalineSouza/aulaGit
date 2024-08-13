cont =  0
soma = 0

while cont <= 1000:
    if (cont % 3 == 0) or (cont % 5 == 0):
        soma = soma + cont
    cont += 1

print(cont)