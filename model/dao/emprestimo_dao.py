from model.dao.data import emprestimos, usuarios, exemplares
from datetime import datetime, date, timedelta
from model.entity.emprestimo import Emprestimo

class EmprestimoDao:

    def __init__(self):
        pass
    
    def check_debito(self):
        for emprestimo in emprestimos:
            if date.today().strftime("%d/%m/%Y") > emprestimo.get_data_devolucao():
                emprestimo.set_debito(True)    

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
        new_id_emprestimo = emprestimos[-1].get_id() + 1
        for usuario in usuarios:
            if usuario.get_id() == usuario_id:
                for exemplar in exemplares:
                    if exemplar.get_numero_exemplares() == numero_exemplar:
                        if not exemplar.get_reserva() and not exemplar.get_emprestimo():
                            if usuario.get_debito() == False:
                                    if (usuario.get_tipo() == 'professor' and usuario.get_emprestimos() < 5) or (usuario.get_tipo() != 'professor' and usuario.get_emprestimos() < 3):
                                        if exemplar.get_circulacao():
                                            if usuario.get_tipo() == 'professor':
                                                exemplar.set_emprestimo(True)
                                                usuario.set_emprestimos(usuario.get_emprestimos() + 1) 
                                                emprestimos.append(Emprestimo(exemplar.get_titulo(), exemplar.get_numero_exemplares(), date.today().strftime("%d/%m/%Y"), (date.today() + timedelta(days=15)).strftime("%d/%m/%Y"), False, int(usuario.get_id()), int(new_id_emprestimo)))
                                                return f'Livro {exemplar.get_titulo()} emprestado para {usuario.get_nome()} até {(date.today() + timedelta(days=15)).strftime("%d/%m/%Y")}.'
                                            else:
                                                exemplar.set_emprestimo(True)
                                                usuario.set_emprestimos(usuario.get_emprestimos() + 1) 
                                                emprestimos.append(Emprestimo(exemplar.get_titulo(), exemplar.get_numero_exemplares(), date.today().strftime("%d/%m/%Y"), (date.today() + timedelta(days=10)).strftime("%d/%m/%Y"), False, int(usuario.get_id()), int(new_id_emprestimo)))
                                                return f'Livro {exemplar.get_titulo()} emprestado para {usuario.get_nome()} até {(date.today() + timedelta(days=10)).strftime("%d/%m/%Y")}.'
                                        else:
                                            exemplar.set_emprestimo(True)
                                            usuario.set_emprestimos(usuario.get_emprestimos() + 1) 
                                            emprestimos.append(Emprestimo(exemplar.get_titulo(), exemplar.get_numero_exemplares(), date.today().strftime("%d/%m/%Y"), (date.today() + timedelta(days=1)).strftime("%d/%m/%Y"), False, int(usuario.get_id()), int(new_id_emprestimo)))
                                            return f'Livro {exemplar.get_titulo()} emprestado para {usuario.get_nome()} até {(date.today() + timedelta(days=1)).strftime("%d/%m/%Y")}.'
                                    else:
                                        return f'Usuário {usuario.get_nome()} ultrapassou o limite de empréstimos.'
                            else:
                                return f'Usuário {usuario.get_nome()} está com débito em atraso'
                        else:
                            return f'Livro {exemplar.get_titulo()} está reservado ou emprestado.'

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
                        for exemplar in exemplares:
                            if exemplar.get_numero_exemplares() == emprestimo.get_exemplar():
                                exemplar.set_emprestimo(False)
                                exemplar.set_reserva(False)
                                emprestimo.set_debito(False)
                                return f'Livro {exemplar.get_titulo()} devolvido.'



        

