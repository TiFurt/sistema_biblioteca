from model.dao.data import emprestimos
from datetime import datetime

class EmprestimoDao:

    def __init__(self):
        pass

    def relatorio_emprestimos(self, input_data_inicial, input_data_final):
        data_inicial = datetime.strptime(input_data_inicial, "%d/%m/%Y")
        data_final = datetime.strptime(input_data_final, "%d/%m/%Y")
        emprestimos_filtrados = []
        for registro in emprestimos:
            data_emprestimo = datetime.strptime(registro.get_data_emprestimo(), "%d/%m/%Y")
            if data_inicial <= data_emprestimo <= data_final:
                emprestimos_filtrados.append(registro)
            else:
                pass
        return emprestimos_filtrados
    
    def novo_emprestimo(self, livro, exemplar, data_emprestimo, data_devolucao, debito, usuario):
        emprestimos.append(f'Emprestimo: {livro}, {exemplar}, {data_emprestimo}, {data_devolucao}, {debito}, {usuario}')
        return

