from model.dao.data import emprestimos
from datetime import datetime

class EmprestimoDao:

    def __init__(self):
        pass

    def relatorio_emprestimos(self, i_data_inicial, i_data_final):
        data_inicial = datetime.strptime(i_data_inicial, "%d/%m/%Y")
        data_final = datetime.strptime(i_data_final, "%d/%m/%Y")
        emprestimos_filtrados = []
        for registro in emprestimos:
            if data_inicial <= registro.get_data_emprestimo() <= data_final:
                emprestimos_filtrados.append(registro)
            else:
                pass
        return emprestimos_filtrados
    
