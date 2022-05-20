class Categoria:
    def __init__(self, nome, descricao, assunto):
        self.nome = nome
        self.descricao = descricao
        self.assunto = assunto

    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome

    def get_descricao(self):
        return self.descricao
    
    def set_descricao(self, descricao):
        self.descricao = descricao

    def get_assunto(self):
        return self.assunto
    
    def set_assunto(self, assunto):
        self.assunto = assunto
   
