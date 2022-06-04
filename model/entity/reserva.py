class Reserva:

    def __init__(self, livro, exemplar, data_reserva, data_vencimento, usuario, id, ativo) -> None:
        self.__livro = livro
        self.__exemplar = exemplar
        self.__data_reserva = data_reserva
        self.__data_vencimento = data_vencimento
        self.__usuario = usuario
        self.__id = id
        self.__ativo = ativo
    
    def get_livro(self):
        return self.__livro
    
    def get_exemplar(self):
        return self.__exemplar
    
    def get_data_reserva(self):
        return self.__data_reserva

    def get_data_vencimento(self):
        return self.__data_vencimento
    
    def get_usuario(self):
        return self.__usuario
    
    def get_id(self):
        return int(self.__id)

    def get_ativo(self):
        return self.__ativo

