from model.dao.data import livros, exemplares

class ExemplarDao:

    def __init__(self):
        pass

    def add_exemplar(self, exemplar):
        exemplares.append(exemplar)