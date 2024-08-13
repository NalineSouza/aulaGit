class Aluno:
    def __init__(self,nome,ra,*args):
        self.__nome = nome
        self.__ra = ra
        self.notas = args


    def getnome(self):
        return self.__nome
    
    def setnome(self):
        return self.__ra
    
    

    