from model.dao.data import livros, exemplares



class LivroDao:

    def __init__(self):
        pass

    def listar_nomes(self):
        nomes = []
        for livro in livros:
            nomes.append(livro.get_titulo())
        return nomes
    
    def add_livro(self, livro):
        livros.append(livro)

    def listar_livros(self):
        return livros
