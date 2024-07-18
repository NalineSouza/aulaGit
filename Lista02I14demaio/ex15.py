nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua segunda nota: "))
res = (nota1 + nota2) / 2

if nota1 >= 0.0 and nota1 <= 10.00:
    print(f"A media da nota1 é {res}")

elif nota2 >= 0.0 and nota2 <= 10.00:
    print(f"A media da nota2 é {res}")

else:
    print("A nota nao é valida!!!")