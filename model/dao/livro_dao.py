from model.dao.data import livros, exemplares



class LivroDao:

    def __init__(self):
        pass

    def listar_nomes(self):
        nomes = []
        for livro in livros:
            nomes.append(livro.get_titulo())
        return nomes

    def get_livro(self, id):
        return livros[id]
    
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

    def alterar_categorias(self, id, categorias):
        livros[id].set_categorias(categorias)
    
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

    def get_nome_categorias(self, id):
        return livros[id].get_nome_categorias()

    def add_exemplar(self, id, exemplar):
        livros[id].add_exemplar(exemplar)

    def get_exemplares(self, id):
        exemplares_livro = []
        livro = livros[id]
        return livro.get_exemplares()

    def format_content(self, content):
        return ''.join(content).strip().upper().replace(' ', '')

    def buscar_titulo(self, titulo):
        titulo_livros = []
        for livro in livros:
            if self.format_content(titulo) in self.format_content(livro.get_titulo()):
                titulo_livros.append(livro)
        return titulo_livros
    
    def buscar_autor(self, autor):
        autores_livros = []
        for livro in livros:
            if self.format_content(autor) in self.format_content(livro.get_autores()):
                autores_livros.append(livro)
        return autores_livros

    def buscar_categoria(self, categoria):
        categoria_livros = []
        for livro in livros:
            if self.format_content(categoria) in self.format_content(livro.get_nome_categorias()):
                categoria_livros.append(livro)
        return categoria_livros

    def consultar_acervo(self, busca):
        resutado_consulta = self.buscar_titulo(busca)
        for livro in self.buscar_autor(busca):
            if livro not in resutado_consulta:
                resutado_consulta.append(livro)
        for livro in self.buscar_categoria(busca):
            if livro not in resutado_consulta:
                resutado_consulta.append(livro)
        return resutado_consulta



