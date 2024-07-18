salarioatual = float(input("Digite o valor do seu salario atual: "))
tempodeserv = int(input("Digite o seu tempo de servico: "))

if (salarioatual <= 500) and (tempodeserv == 1):
    reajuste = salarioatual * 0.25
    res = reajuste + salarioatual
    print(f"O valor do reajuste do seu salario  é {res}\nO senhor nao possui bonus de salario!")

elif (salarioatual > 500) and (salarioatual <= 1000) and (tempodeserv > 1) and (tempodeserv <= 3):
    reajuste = (salarioatual * 0.20) + 100
    res = reajuste + salarioatual
    print(f"O valor do reajuste do seu salario  é {res}\nO senhor possui um  bonus de salario!")

elif (salarioatual > 1000) and (salarioatual <= 1500) and (tempodeserv >= 4) and (tempodeserv <= 6):
    reajuste = (salarioatual * 0.15) + 200
    res = reajuste + salarioatual
    print(f"O valor do reajuste do seu salario  é {res}\nO senhor possui bonus de salario!")

elif (salarioatual > 1500) and (salarioatual <= 2000) and (tempodeserv >= 7) and (tempodeserv <= 10):
    reajuste = (salarioatual * 0.10) + 300
    res = reajuste + salarioatual
    print(f"O valor do reajuste do seu salario  é {res}\nO senhor possui bonus de salario!")

elif (salarioatual > 2000) and (tempodeserv > 10):
    res = salarioatual + 500
    print(f"O senhor não possui um reajuste de sálario\nO senhor possui bonus, e os seu salario a partir de hoje é {res}")

    
