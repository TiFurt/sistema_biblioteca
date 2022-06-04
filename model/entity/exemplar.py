from model.entity.livro import Livro


class Exemplar(Livro):
    def __init__(self, titulo, autores, ano, isbn, edicao, editora, categorias, numero_exemplar, circulacao, emprestimo ,reservado) -> None:
        Livro.__init__(self, titulo, autores, ano, isbn, edicao, editora, categorias)
        self.__numero_exemplar = numero_exemplar
        self.__circulacao = circulacao
        self.__emprestimo = emprestimo
        self.__is_reservado = reservado
        self.__reserva = None

    def get_numero_exemplares(self):
        return self.__numero_exemplar

    def get_circulacao(self):
        return self.__circulacao

    def get_emprestimo(self):
        return self.__emprestimo

    def is_reservado(self):
        return self.__is_reservado

    def set_reserva(self, reserva):
        self.__reserva = reserva
        self.__is_reservado = True

    def set_not_reservado(self):
        self.__reserva = None
        self.__is_reservado = False

    def get_reserva(self):
        return self.__reserva
    
    def set_numero_exemplar(self, numero_exemplar):
        self.__numero_exemplar = numero_exemplar

    def set_circulacao(self, circulacao):
        self.__circulacao = circulacao

    def set_emprestimo(self, emprestimo):
        self.__emprestimo = emprestimo

