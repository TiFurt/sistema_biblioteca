class Usuario:
    def __init__(self, id, nome, tipo, debito=False, emprestimos=0):
        self.__id = id
        self.__nome = nome
        self.__tipo = tipo
        self.__debito = debito
        self.__emprestimos = emprestimos
    
    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_tipo(self):
        return self.__tipo

    def get_debito(self):
        return self.__debito

    def get_emprestimos(self):
        return self.__emprestimos
    
    def set_id(self, id):
        self.__id = id
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_tipo(self, tipo):
        self.__tipo = tipo
    
    def set_debito(self, debito):
        self.__debito = debito
    
    def set_emprestimos(self, emprestimos):
        self.__emprestimos = emprestimos