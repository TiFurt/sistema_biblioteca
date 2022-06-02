from model.dao.data import emprestimos, usuarios, exemplares
from datetime import datetime, date, timedelta

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
    
    def novo_emprestimo(self, usuario_id, numero_exemplar):
        for usuario in usuarios:
            if usuario.get_id() == usuario_id:
                for exemplar in exemplares:
                    if exemplar.get_numero_exemplares() == numero_exemplar:
                        if exemplar.get_reserva() == False and exemplar.get_emprestimo() == False:
                            if usuario.get_debito() == False:
                                    if (usuario.get_tipo() == 'professor' and usuario.get_emprestimos() < 5) or (usuario.get_tipo() != 'professor' and usuario.get_emprestimos() < 3):
                                        if exemplar.get_circulacao() == True:
                                            if usuario.get_tipo() == 'professor':
                                                exemplar.set_emprestimo(True)
                                                emprestimos.append(f'Emprestimo({exemplar.get_titulo()}, {exemplar.get_numero_exemplares()}, {date.today().strftime("%d/%m/%Y")}, {(date.today() + timedelta(days=15)).strftime("%d/%m/%Y")}, {False}, {usuario.get_id()}),')
                                                return f'Livro {exemplar.get_titulo()} emprestado para {usuario.get_nome()} até {(date.today() + timedelta(days=15)).strftime("%d/%m/%Y")}.'
                                            else:
                                                exemplar.set_emprestimo(True)
                                                emprestimos.append(f'Emprestimo({exemplar.get_titulo()}, {exemplar.get_numero_exemplares()}, {date.today().strftime("%d/%m/%Y")}, {(date.today() + timedelta(days=10)).strftime("%d/%m/%Y")}, {False}, {usuario.get_id()}),')
                                                return f'Livro {exemplar.get_titulo()} emprestado para {usuario.get_nome()} até {(date.today() + timedelta(days=10)).strftime("%d/%m/%Y")}.'
                                        else:
                                            exemplar.set_emprestimo(True)
                                            emprestimos.append(f'Emprestimo({exemplar.get_titulo()}, {exemplar.get_numero_exemplares()}, {date.today().strftime("%d/%m/%Y")}, {(date.today() + timedelta(days=1)).strftime("%d/%m/%Y")}, {False}, {usuario.get_id()}),')
                                            return f'Livro {exemplar.get_titulo()} emprestado para {usuario.get_nome()} até {(date.today() + timedelta(days=1)).strftime("%d/%m/%Y")}.'
                                    else:
                                        return f'Usuário {usuario.get_nome()} ultrapassou o limite de empréstimos.'
                            else:
                                return f'Usuário {usuario.get_nome()} está com débito em atraso'
                        else:
                            return f'Livro {exemplar.get_titulo()} está reservado ou emprestado.'
                    else:
                        return f'Exemplar {numero_exemplar} não existe'
            else:
                return f'Usuário com id {usuario_id} não existe'

