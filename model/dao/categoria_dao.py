from model.dao.data import categorias

class CategoriaDao:

    def __init__(self):
        pass

    def listar(self):
        return categorias

    def listar_nomes(self):
        nomes = []
        for categoria in categorias:
            nomes.append(categoria.get_nome())
        return nomes

    def add_categoria(self, categoria):
        categorias.append(categoria)

    def remover_categoria(self, id_excluir):
        categorias.pop(id_excluir)

    def alterar_nome(self, id, nome):
        categorias[id].set_nome(nome)
    
    def alterar_descricao(self, id, descricao):
        categorias[id].set_descricao(descricao)
    
    def alterar_assunto(self, id, assunto):
        categorias[id].set_assunto(assunto)