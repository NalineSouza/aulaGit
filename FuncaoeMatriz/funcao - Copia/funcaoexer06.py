def gerar_tabela_preco():
    preco_unitario = 1.99
    for quantidade in range(1, 51):
        print(f"{quantidade} item(s): R$ {quantidade * preco_unitario:.2f}")

'''
{quantidade * preco_unitario}
     1      *    1.99         = 1.99
     2      *    1.99         = 3.98
     3      *    1.99         = 5.97

'''

gerar_tabela_preco()