








def calcula(**kwargs):
    val = kwargs['valor']
    perc = kwargs['porcentagem']
    resultado = val * perc / 100
    return resultado



x = calcula(idade=18,valor=89,nome="maria",porcentagem=500)

print(x)