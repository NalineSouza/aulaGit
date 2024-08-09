numero1 = int(input("Digite seu numero: "))
numero2 = int(input("Digite seu numero: "))

print(f"Seu valor é {numero1}")
print(f"Seu valor é {numero2}")

varvazia = numero1
numero1 = numero2
numero2 = varvazia


print(f"Agora seu numero é {numero1}")
numero2 = numero1
print(f"Agora seu numero é {varvazia}")