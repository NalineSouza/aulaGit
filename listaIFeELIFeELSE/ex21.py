not1 = float(input("Digite sua nota de laboratorio: "))
not2 = float(input("Digite a nota da avaliacao semestral: "))
not3 = float(input("Digite a nota do exame final: "))

mediaf = ((not1 * 0.2) + (not2 * 0.3) + (not3 * 0.5))

if 0 <= mediaf <= 2.9:
    print("Voce foi reprovado!!")

elif 3 <= mediaf <= 5.9:
    print("Voce ficou de recuperacao!!")

else:
    print(f"Voce passou com media {mediaf}")
