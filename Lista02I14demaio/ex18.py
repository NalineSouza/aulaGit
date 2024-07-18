altura = float(input("Digite sua altura : "))
sexo = input("Digite seu sexo (M-Mascilino /F-Feminino): ")

if sexo == 'M':
    homens =(72.7 * altura) - 58
    print(f"Seu peso ideal é {homens:.1f}")

elif sexo == 'F':
    mulher = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é {mulher:.1f}")

else:
    print("Digite um sexo valido!!")