class Cachorro:
    ##SEMPRE COMEÇAR PELO MÉTODO CONSTRUTOR
    def __init__(self,nome,idade,peso,cor="Preto"):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.cor = cor

    #MÉTODOS...... todos os metodos devem ter como parametro SELF
        
    def latir(self):
        print(f"{self.nome} AU AU")

    def comer(self):
        print(f"")