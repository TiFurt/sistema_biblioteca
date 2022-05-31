from model.entity.livro import Livro


class Exemplar(Livro):
    def __init__(self, titulo, autores, ano, isbn, edicao, editora, categorias, numero_exemplar, circulacao) -> None:
        Livro.__init__(self, titulo, autores, ano, isbn, edicao, editora, categorias)
        self.__numero_exemplar = numero_exemplar
        self.__circulacao = circulacao

    def get_numero_exemplares(self):
        return self.__numero_exemplar

    def get_circulacao(self):
        return self.__circulacao

    def set_numero_exemplar(self, numero_exemplar):
        self.__numero_exemplar = numero_exemplar

    def set_circulacao(self, circulacao):
        self.__circulacao = circulacao