from model.dao.data import reservas, usuarios, livros
from datetime import date, timedelta, datetime
from model.entity.reserva import Reserva

class ReservaDao:

    def __init__(self) -> None:
        for reserva in reservas:
            if date.today().strftime("%d/%m/%Y") > reserva.get_data_vencimento():
                reserva.set_ativo(False)  
        pass

    def nova_reserva(self, usuario_id, livro_id, numero_exemplar):
        new_id_reserva = reservas[-1].get_id() + 1
        for usuario in usuarios:
            if usuario.get_id() == usuario_id and livros[livro_id].get_numero_exemplares() != 0:
                if livros[livro_id].get_numero_exemplares() != 0:
                    exemplar = livros[livro_id].get_exemplares()[numero_exemplar]
                    if not exemplar.is_reservado():
                        if not usuario.get_debito():
                            if exemplar.get_circulacao():
                                if not exemplar.get_emprestimo():
                                    usuario.set_emprestimos(usuario.get_emprestimos() + 1) 
                                    if usuario.get_tipo() == 'professor':
                                        reserva = Reserva(exemplar.get_titulo(), exemplar.get_numero_exemplares(), date.today().strftime("%d/%m/%Y"), (date.today() + timedelta(days=15)).strftime("%d/%m/%Y"), int(usuario.get_id()), int(new_id_reserva), True)
                                        exemplar.set_reserva(reserva)
                                        reservas.append(reserva)
                                        return f'Livro {exemplar.get_titulo()} reservado para {usuario.get_nome()} até {(date.today() + timedelta(days=15)).strftime("%d/%m/%Y")}.'
                                    else:
                                        reserva = Reserva(exemplar.get_titulo(), exemplar.get_numero_exemplares(), date.today().strftime("%d/%m/%Y"), (date.today() + timedelta(days=10)).strftime("%d/%m/%Y"), int(usuario.get_id()), int(new_id_reserva), True)
                                        exemplar.set_reserva(reserva)
                                        reservas.append(reserva)
                                        return f'Livro {exemplar.get_titulo()} reservado para {usuario.get_nome()} até {(date.today() + timedelta(days=10)).strftime("%d/%m/%Y")}.'
                                else:
                                    data_fim_emprestimo = exemplar.get_emprestimo_atual().get_data_devolucao()
                                    if usuario.get_tipo() == 'professor':
                                        reserva = Reserva(exemplar.get_titulo(), exemplar.get_numero_exemplares(), data_fim_emprestimo, (data_fim_emprestimo + timedelta(days=15)).strftime("%d/%m/%Y"), int(usuario.get_id()), int(new_id_reserva), True)
                                        exemplar.set_reserva(reserva)
                                        reservas.append(Reserva(reserva))
                                        return f'Livro {exemplar.get_titulo()} reservado para {usuario.get_nome()} até {(date.today() + timedelta(days=15)).strftime("%d/%m/%Y")}.'
                                    else:
                                        reserva = Reserva(exemplar.get_titulo(), exemplar.get_numero_exemplares(), data_fim_emprestimo, (data_fim_emprestimo + timedelta(days=10)).strftime("%d/%m/%Y"), int(usuario.get_id()), int(new_id_reserva), True)
                                        exemplar.set_reserva(reserva)
                                        reservas.append(reserva)
                                        return f'Livro {exemplar.get_titulo()} reservado para {usuario.get_nome()} até {(date.today() + timedelta(days=10)).strftime("%d/%m/%Y")}.'
                            else:
                                return f'Este exemplar do livro {exemplar.get_titulo()} não está disponível para circulação.'
                        else:
                            return f'Usuario {usuario.get_nome()} está em debito.'
                    else:
                        return f'Este exemplar do livro {exemplar.get_titulo()} já está reservado.'
                else:
                    return f'Livro {exemplar.get_titulo()} não possui exemplares.'

    def relatorio_reservas(self, input_data_inicial, input_data_final):
        data_inicial = datetime.strptime(input_data_inicial, "%d/%m/%Y")
        data_final = datetime.strptime(input_data_final, "%d/%m/%Y")
        emprestimos_filtrados = []
        for registro in reservas:
            data_reserva = datetime.strptime(registro.get_data_reserva(), "%d/%m/%Y")
            if data_inicial <= data_reserva <= data_final:
                emprestimos_filtrados.append(registro)
            else:
                pass
        return emprestimos_filtrados
    
    def pendencias_reserva(self, usuario_id):
        pendencias = []
        for usuario in usuarios:
            for reserva in reservas:
                if reserva.get_usuario() == usuario_id:
                    if usuario.get_id() == usuario.get_id():
                        if reserva.get_data_vencimento() > date.today().strftime("%d/%m/%Y"):
                            pendencias.append(reserva)
                    return pendencias

    def cancelamento_reserva(self, reserva_id):
        for reserva in reservas:
            if reserva.get_id() == reserva_id:
                reserva.set_data_vencimento(date.today().strftime("%d/%m/%Y"))
                for usuario in usuarios:
                    if usuario.get_id() == reserva.get_usuario():
                        usuario.set_emprestimos(usuario.get_emprestimos() - 1)
                        for livro in livros:
                            if livro.get_titulo() == reserva.get_livro() and livro.get_numero_exemplares() != 0:
                                exemplar = livro.get_exemplares()[reserva.get_exemplar()-1]
                                exemplar.set_not_reservado()
                                reserva.set_ativo(False)
                                return f'Reserva do livro {exemplar.get_titulo()} cancelada.'
