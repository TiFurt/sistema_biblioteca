from model.dao.data import emprestimos, usuarios, livros
from datetime import datetime, date, timedelta
from model.entity.emprestimo import Emprestimo

class EmprestimoDao:

    def __init__(self):
        for emprestimo in emprestimos:
            if date.today().strftime("%d/%m/%Y") > emprestimo.get_data_devolucao():
                emprestimo.set_debito(True)  
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
    
    def novo_emprestimo(self, usuario_id, livro_id, numero_exemplar):
        new_id_emprestimo = emprestimos[-1].get_id() + 1
        for usuario in usuarios:
            if usuario.get_id() == usuario_id:
                if livros[livro_id].get_numero_exemplares() != 0:
                    exemplar = livros[livro_id].get_exemplares()[numero_exemplar]
                    if not exemplar.get_emprestimo():
                        if not exemplar.is_reservado() or (exemplar.is_reservado() and usuario_id ==  exemplar.get_reserva().get_usuario()):
                            if exemplar.is_reservado():
                                usuario.set_emprestimos(usuario.get_emprestimos - 1)
                            exemplar.set_not_reservado()
                            if not usuario.get_debito():
                                if (usuario.get_tipo() == 'professor' and usuario.get_emprestimos() < 5) or (usuario.get_tipo() != 'professor' and usuario.get_emprestimos() < 3):
                                    usuario.set_emprestimos(usuario.get_emprestimos() + 1) 
                                    if exemplar.get_circulacao():
                                        if usuario.get_tipo() == 'professor':
                                            emprestimo = Emprestimo(exemplar.get_titulo(), exemplar.get_numero_exemplares(), date.today().strftime("%d/%m/%Y"), (date.today() + timedelta(days=15)).strftime("%d/%m/%Y"), False, int(usuario.get_id()), int(new_id_emprestimo))
                                            exemplar.set_emprestimo_atual(emprestimo)
                                            emprestimos.append(emprestimo)
                                            return f'Livro {exemplar.get_titulo()} emprestado para {usuario.get_nome()} at?? {(date.today() + timedelta(days=15)).strftime("%d/%m/%Y")}.'
                                        else:
                                            emprestimo = Emprestimo(exemplar.get_titulo(), exemplar.get_numero_exemplares(), date.today().strftime("%d/%m/%Y"), (date.today() + timedelta(days=10)).strftime("%d/%m/%Y"), False, int(usuario.get_id()), int(new_id_emprestimo))
                                            exemplar.set_emprestimo_atual(emprestimo)
                                            emprestimos.append(emprestimo)
                                            return f'Livro {exemplar.get_titulo()} emprestado para {usuario.get_nome()} at?? {(date.today() + timedelta(days=10)).strftime("%d/%m/%Y")}.'
                                    else:
                                        emprestimo = Emprestimo(exemplar.get_titulo(), exemplar.get_numero_exemplares(), date.today().strftime("%d/%m/%Y"), (date.today() + timedelta(days=1)).strftime("%d/%m/%Y"), False, int(usuario.get_id()), int(new_id_emprestimo))
                                        exemplar.set_emprestimo(emprestimo)
                                        emprestimos.append(emprestimo)
                                        return f'Livro {exemplar.get_titulo()} emprestado para {usuario.get_nome()} at?? {(date.today() + timedelta(days=1)).strftime("%d/%m/%Y")}.'
                                else:
                                    return f'Usu??rio {usuario.get_nome()} ultrapassou o limite de empr??stimos.'
                            else:
                                return f'Usu??rio {usuario.get_nome()} est?? com d??bito em atraso'
                        else:
                            return f'Livro {exemplar.get_titulo()} est?? reservado para outro usu??rio.'
                    else:
                        return f'Livro {exemplar.get_titulo()} est?? emprestado.'
                else:
                    return f'Livro {livros[livro_id].get_titulo()} n??o possui exemplares.'

    def pendencias_emprestimo(self, usuario_id):
        pendencias = []
        for usuario in usuarios:
            for emprestimo in emprestimos:
                if emprestimo.get_usuario() == usuario_id:
                    if usuario.get_id() == usuario.get_id():
                        if emprestimo.get_debito() or emprestimo.get_data_devolucao() > date.today().strftime("%d/%m/%Y"):
                            pendencias.append(emprestimo)
                    return pendencias

    def devolucao_emprestimo(self, emprestimo_id):
        for emprestimo in emprestimos:
            if emprestimo.get_id() == emprestimo_id:
                emprestimo.set_data_devolucao(date.today().strftime("%d/%m/%Y"))
                for usuario in usuarios:
                    if usuario.get_id() == emprestimo.get_usuario():
                        usuario.set_emprestimos(usuario.get_emprestimos() - 1)
                        for livro in livros:
                            if livro.get_titulo() == emprestimo.get_livro() and livro.get_numero_exemplares() != 0:
                                exemplar = livro.get_exemplares()[emprestimo.get_exemplar()-1]
                                exemplar.set_not_emprestado()
                                emprestimo.set_debito(False)
                                return f'Livro {exemplar.get_titulo()} devolvido.'

    def relatorio_pendencias(self, input_data_inicial, input_data_final):
        pendencias = []
        data_inicial = datetime.strptime(input_data_inicial, "%d/%m/%Y")
        data_final = datetime.strptime(input_data_final, "%d/%m/%Y")
        for registro in emprestimos:
                    data_emprestimo = datetime.strptime(registro.get_data_emprestimo(), "%d/%m/%Y")
                    if data_inicial <= data_emprestimo <= data_final:
                        if registro.get_debito():
                            pendencias.append(registro)
                    else:
                        pass
                    return pendencias        

