class livro:
    def __init__(self,nome,autor,edit,pags):
        self.name = nome
        self.autor = autor
        self.edit = edit
        self.pags = pags


    def listaQtPags(self):
        for i in range(self.paginas):
            print(i)

    def alterarEditora(self,novaEditora):
        self.editora = novaEditora

livro1 = livro("MEMORIAS")