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

    def remover_livro(self, id_livro_excluir):
        livros.pop(id_livro_excluir)

    def listar_livros(self):
        return livros

    def alterar_titulo(self, id, titulo):
        livros[id].set_titulo(titulo)

    def alterar_autores(self, id, autores):
        livros[id].set_autores(autores)
    
    def alterar_ano(self, id, ano):
        livros[id].set_ano(ano)

    def alterar_isbn(self, id, isbn):
        livros[id].set_isbn(isbn)

    def alterar_edicao(self, id, edicao):
        livros[id].set_edicao(edicao)

    def alterar_editora(self, id, editora):
        livros[id].set_editora(editora)

    def alterar_assuntos(self, id, assuntos):
        livros[id].set_assuntos(assuntos)
    
    def get_titulo(self, id):
        return livros[id].get_titulo()

    def get_autores(self, id):
        return livros[id].get_autores()

    def get_ano(self, id):
        return livros[id].get_ano()

    def get_isbn(self, id):
        return livros[id].get_isbn()

    def get_edicao(self, id):
        return livros[id].get_edicao()

    def get_editora(self, id):
        return livros[id].get_editora()

    def get_assuntos(self, id):
        return livros[id].get_assuntos()

    def add_exemplar(self, id, exemplar):
        livros[id].add_exemplar(exemplar)

    def get_exemplares(self, id):
        exemplares_livro = []
        livro = livros[id]
        return livro.get_exemplares()

    def buscar_livro(self, titulo):
        for livro in livros:
            if livro.get_titulo() == titulo:
                return livro
        return None




