nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))


mf = (nota1 + nota2) + (nota3 * 2) / 3

if mf >= 60:
    print(f"Sua media é de {mf}, parabens voce passou!!")

else:
    print("Voce foi REPROVADO.")