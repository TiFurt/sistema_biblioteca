class Emprestimo:

    def __init__(self, livro, exemplar, data_emprestimo, data_devolucao, debito, usuario, id) -> None:
        self.__livro = livro
        self.__exemplar = exemplar
        self.__data_emprestimo = data_emprestimo
        self.__data_devolucao = data_devolucao
        self.__debito = debito
        self.__usuario = usuario
        self.__id = id
    
    def get_livro(self):
        return self.__livro
    
    def get_exemplar(self):
        return self.__exemplar
    
    def get_data_emprestimo(self):
        return self.__data_emprestimo
    
    def get_data_devolucao(self):
        return self.__data_devolucao
    
    def get_debito(self):
        return self.__debito

    def get_usuario(self):
        return self.__usuario

    def get_id(self):
        return int(self.__id)

    def set_debito(self, debito):
        self.__debito = debito

    def set_data_devolucao(self, data_devolucao):
        self.__data_devolucao = data_devolucao