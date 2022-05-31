class Livro:
    def __init__(self, titulo, autores, ano, isbn, edicao, editora, categorias) -> None:
        self.__titulo = titulo
        self.__autores = autores
        self.__ano = ano
        self.__isbn = isbn
        self.__edicao = edicao
        self.__editora = editora
        self.__categorias = categorias
        self.__exemplares = []
        self.__numero_exemplar = 0

    def get_titulo(self) -> str:
        return self.__titulo

    def get_autores(self) -> list:
        return self.__autores

    def get_ano(self) -> int:
        return self.__ano

    def get_isbn(self) -> str:
        return self.__isbn

    def get_edicao(self) -> int:
        return self.__edicao

    def get_editora(self) -> str:
        return self.__editora

    def get_categorias(self) -> list:
        return self.__categorias
    
    def get_nome_categorias(self) -> list:
        nomes_categorias = []
        for categoria in self.get_categorias():
            nomes_categorias.append(categoria.get_nome())
        return nomes_categorias

    def set_titulo(self, titulo) -> None:
        self.__titulo = titulo

    def set_autores(self, autores) -> None:
        self.__autores = autores

    def set_ano(self, ano) -> None:
        self.__ano = ano

    def set_isbn(self, isbn) -> None:
        self.__isbn = isbn

    def set_edicao(self, edicao) -> None:
        self.__edicao = edicao

    def set_editora(self, editora) -> None:
        self.__editora = editora

    def set_categorias(self, categorias) -> list:
        self.__categorias = categorias

    def get_exemplares(self) -> list:
        return self.__exemplares

    def add_exemplar(self, exemplar) -> None:
        self.__exemplares.append(exemplar)
        self.__numero_exemplar += 1

    def remove_exemplar(self, exemplar) -> None:
        self.__exemplares.remove(exemplar)
        self.__numero_exemplar -= 1

    def get_numero_exemplares(self) -> int:
        return self.__numero_exemplar

    def check_exemplar(self):
        if self.get_exemplares() == []:
            return True
        return False

    
