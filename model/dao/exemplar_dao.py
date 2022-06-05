from model.dao.data import exemplares

class ExemplarDao:

    def __init__(self):
        pass

    @staticmethod
    def listar():
        return exemplares

    @staticmethod
    def listar_nomes():
        nomes = []
        for exemplar in exemplares:
            nomes.append(exemplar.get_titulo())
        return nomes

    @staticmethod
    def add_exemplar(exemplar):
        exemplares.append(exemplar)

    def remover_exemplar(self, id_excluir):
        exemplares.pop(id_excluir)

    def alterar_numero(self, id, numero):
        exemplares[id].set_numero(numero)

    def alterar_circulacao(self, id, circulacao):
        exemplares[id].set_circulacao(circulacao)


    