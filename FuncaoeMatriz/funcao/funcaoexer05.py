'''
Escreva um programa com um função chamada somaImposto. A função possui dois
parâmetros formais:taxaImposto, que é a quantia de imposto sobre vendas
expressa em porcentagem e custo, que é o custo de um item antes do imposto. 
A função 'altera' o valor de custo para incluir o imposto sobre vendas. por
fim deve retornar o novo valor para o usuario considerando o percentual
do imposto.

'''
def soma_imposto(taxa_imposto,valorproduto):
     res = valorproduto + (valorproduto * taxa_imposto) / 100
     return res





valorproduto = int(input("Digite o valor do produto: "))
taxa_imposto = float(input("Digite o valor da taxa: "))


resultado = soma_imposto(taxa_imposto,valorproduto)

print(resultado)


