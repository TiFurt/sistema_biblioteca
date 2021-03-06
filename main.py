from select import select
from model.dao.livro_dao import LivroDao
from model.dao.exemplar_dao import ExemplarDao
from model.dao.categoria_dao import CategoriaDao
from model.dao.emprestimo_dao import EmprestimoDao
from model.dao.reserva_dao import ReservaDao
from model.dao.usuario_dao import UsuarioDao
from model.entity.livro import Livro
from model.entity.exemplar import Exemplar
from model.entity.categoria import Categoria

if __name__ == '__main__':
    livro_dao = LivroDao()
    exemplar_dao = ExemplarDao()
    categoria_dao = CategoriaDao()
    emprestimo_dao = EmprestimoDao()
    reserva_dao = ReservaDao()
    usuario_dao = UsuarioDao()

    try:

        while True:
            print('''
                Escolha uma das opções abaixo:
                1 - Bibliotecário
                2 - Usuário da Biblioteca
                3 - Gerente da Biblioteca
                4 - Funcionário de Atendimento
                0 - Sair''')
            usuario = int(input('Informe o Tipo de Usuário: '))
            match usuario:
                case 0:  # sair
                    print('Saindo...')
                    break
                case 1:  # Bibliotecário
                    while True:
                        print('''
                            Menu bibliotecário:
                            Escolha uma das opções abaixo
                            1 - Livros
                            2 - Exemplares
                            3 - Categorias
                            0 - Sair''')
                        opcao_menu = int(input('Digite sua opção(0 para sair): '))
                        match opcao_menu:
                            case 0:
                                print('Saindo...')
                                break
                            case 1:
                                print('''
                                    Menu Livros
                                    Escolha uma das opções abaixo:
                                    1 - Cadastrar Livros
                                    2 - Alterar dados  de um Livro
                                    3 - Consultar Dados de um Livro
                                    4 - Excluir um Livro
                                    0 - Sair''')
                                opcao_livro = int(input('Digite sua opção(0 para sair): '))
                                match opcao_livro:
                                    case 0:
                                        print('Saindo...')
                                        pass

                                    case 1:
                                        titulo = input('Insira o título do livro: ')
                                        autores = []
                                        while True:
                                            autor = input('Insira o autor do livro(0 para continuar): ')
                                            if autor == '0':
                                                break
                                            autores.append(autor)

                                        ano = int(input('Insira o ano de publicação do livro: '))
                                        isbn = int(input('Insira o ISBN do livro: '))
                                        edicao = input('Insira a edição do livro: ')
                                        editora = input('Insira a editora do livro: ')
                                        categorias = []
                                        while True:
                                            print('Escolha as Categorias do Livro: ')
                                            contc = 0
                                            for categoria in categoria_dao.listar_nomes():
                                                contc += 1
                                                print(f'{contc} - {categoria}')
                                            id_categoria_adicionar_livro = int(
                                                input('Escolha a categoria (0 para continuar): ')) - 1
                                            if id_categoria_adicionar_livro == -1:
                                                break
                                            elif categoria_dao.get_categoria(
                                                    id_categoria_adicionar_livro) in categorias:
                                                print('Categoria já adicionada!')
                                                input('Pressione enter para continuar...')
                                            else:
                                                categorias.append(
                                                    categoria_dao.get_categoria(id_categoria_adicionar_livro))
                                                print(
                                                    f'Categoria {categoria_dao.get_nome(id_categoria_adicionar_livro)} adicionada com sucesso!')

                                        livro_dao.add_livro(
                                            Livro(titulo, autores, ano, isbn, edicao, editora, categorias))
                                        print(f'Livro {titulo} cadastrado com sucesso!')
                                        pass

                                    case 2:
                                        print('Escolha um livro para alterar: ')
                                        cont = 0
                                        for livro in livro_dao.listar_nomes():
                                            cont += 1
                                            print(f'{cont} - {livro}')
                                        escolha_livro = int(input('Digite sua opção: ')) - 1
                                        livro = livro_dao.get_livro(escolha_livro)
                                        print(f'''
                                            1- Titulo: {livro.get_titulo()}
                                            2- Autor: {', '.join(livro.get_autores())}
                                            3- Ano: {livro.get_ano()}
                                            4- ISBN: {livro.get_isbn()}
                                            5- Edicao: {livro.get_edicao()}
                                            6- Editora: {livro.get_editora()}
                                            7- Assuntos: {', '.join(livro.get_nome_categorias())}
                                            0- Sair''')
                                        opcao_alteracao = int(input('Digite sua opção(0 para sair): '))
                                        match opcao_alteracao:
                                            case 0:
                                                print('Saindo...')
                                                pass

                                            case 1:
                                                titulo_alteracao = input('Insira o título do livro: ')
                                                livro_dao.alterar_titulo(escolha_livro, titulo_alteracao)
                                                print(f'Título alterado para {titulo_alteracao}')

                                            case 2:
                                                autores_alteracao = []
                                                while True:
                                                    autor_alteracao = input(
                                                        'Insira os autores do livro(0 para continuar): ')
                                                    if autor_alteracao == '0':
                                                        break
                                                    autores_alteracao.append(autor_alteracao)
                                                livro_dao.alterar_autores(escolha_livro, autores_alteracao)
                                                print(f'Autores alterados para {", ".join(autores_alteracao)}')

                                            case 3:
                                                ano_alteracao = input('Insira o ano do livro: ')
                                                livro_dao.alterar_ano(escolha_livro, ano_alteracao)
                                                print(f'Ano alterado para {ano_alteracao}')

                                            case 4:
                                                isbn_alteracao = input('Insira o isbn do livro: ')
                                                livro_dao.alterar_isbn(escolha_livro, isbn_alteracao)
                                                print(f'Isbn alterado para {isbn_alteracao}')

                                            case 5:
                                                edicao_alteracao = input('Insira a edição do livro: ')
                                                livro_dao.alterar_edicao(escolha_livro, edicao_alteracao)
                                                print(f'Edição alterada para {edicao_alteracao}')

                                            case 6:
                                                editora_alteracao = input('Insira a editora do livro: ')
                                                livro_dao.alterar_editora(escolha_livro, editora_alteracao)
                                                print(f'Editora alterada para {editora_alteracao}')

                                            case 7:
                                                categorias = []
                                                while True:
                                                    print('Escolha as Categorias do Livro: ')
                                                    contc = 0
                                                    for categoria in categoria_dao.listar_nomes():
                                                        contc += 1
                                                        print(f'{contc} - {categoria}')
                                                    id_alterar_categoria_livro = int(
                                                        input('Escolha a categoria (0 para continuar): ')) - 1
                                                    if id_alterar_categoria_livro == -1:
                                                        break
                                                    elif categoria_dao.get_categoria(
                                                            id_alterar_categoria_livro) in categorias:
                                                        print('Categoria já adicionada!')
                                                        input('Pressione enter para continuar...')
                                                    else:
                                                        categorias.append(
                                                            categoria_dao.get_categoria(id_alterar_categoria_livro))
                                                        print(
                                                            f'Categoria {categoria_dao.get_nome(id_alterar_categoria_livro)} adicionada com sucesso!')
                                                        input('Pressione enter para continuar...')
                                                livro_dao.alterar_categorias(escolha_livro, categorias)

                                        pass

                                    case 3:
                                        print('Escolha um livro para consultar: ')
                                        contc = 0
                                        for livro in livro_dao.listar_nomes():
                                            contc += 1
                                            print(f'{contc} - {livro}')
                                        escolha_consulta = int(input('Digite sua opção(0 para sair): ')) - 1
                                        if escolha_consulta == -1:
                                            print('Saindo...')
                                            pass
                                        else:
                                            consulta = livro_dao.listar_livros()[escolha_consulta]
                                            print(f'''
                                                Titulo: {consulta.get_titulo()}
                                                Autor: {', '.join(consulta.get_autores())}
                                                Ano: {consulta.get_ano()}
                                                ISBN: {consulta.get_isbn()}
                                                Edicao: {consulta.get_edicao()}
                                                Editora: {consulta.get_editora()}
                                                Assuntos: {', '.join(consulta.get_nome_categorias())}
                                                Sair''')
                                            input('Pressione enter para continuar...')
                                            pass

                                    case 4:
                                        print('Escolha um livro para excluir: ')
                                        cont = 0
                                        for livro in livro_dao.listar_nomes():
                                            cont += 1
                                            print(f'{cont} - {livro}')
                                        id_livro_excluir = int(input('Digite sua opção(0 para sair): ')) - 1
                                        if id_livro_excluir == -1:
                                            print('Saindo...')
                                            pass
                                        else:
                                            if livro_dao.listar_livros()[id_livro_excluir].check_exemplar():
                                                validacao = input(
                                                    f'Tem certeza que deseja excluir o livro {livro_dao.get_titulo(id_livro_excluir)}?(S/N) ').upper()
                                                if validacao.split()[0][0] == 'S':
                                                    print(
                                                        f'Livro {livro_dao.get_titulo(id_livro_excluir)} excluido com sucesso!')
                                                    livro_dao.remover_livro(id_livro_excluir)
                                                else:
                                                    print('Saindo...')
                                                pass
                                            else:
                                                print('Não é possível excluir um livro com exemplares!')
                                                input('Pressione enter para continuar...')
                                                pass
                                            pass
                                pass

                            case 2:
                                print('''
                                        Escolha uma das opções abaixo:
                                        1 - Cadastrar Exemplar
                                        2 - Alterar dados de um Exemplar
                                        3 - Consultar Dados de um Exemplar
                                        4 - Excluir um Exemplar
                                        0 - Sair''')
                                opcao_exemplar = int(input('Digite sua opção(0 para sair): '))
                                match opcao_exemplar:
                                    case 0:
                                        print('Saindo...')
                                        pass

                                    case 1:
                                        print('Escolha um livro para cadastrar um exemplar: ')
                                        cont = 0
                                        for livro in livro_dao.listar_nomes():
                                            cont += 1
                                            print(f'{cont} - {livro}')
                                        id_livro_cadastrar = int(input('Digite sua opção(0 para sair): ')) - 1
                                        if id_livro_cadastrar == -1:
                                            print('Saindo...')
                                            pass
                                        else:
                                            circulacao = input('O exemplar poderá ser emprestado?(S/N) ').upper()
                                            if circulacao.split()[0][0] == 'S':
                                                circulacao = True
                                            else:
                                                circulacao = False
                                                pass
                                            livro_toexemplar = livro_dao.listar_livros()[id_livro_cadastrar]
                                            livro_dao.add_exemplar(id_livro_cadastrar,
                                                                   Exemplar(livro_toexemplar.get_titulo(),
                                                                            livro_toexemplar.get_autores(),
                                                                            livro_toexemplar.get_ano(),
                                                                            livro_toexemplar.get_isbn(),
                                                                            livro_toexemplar.get_edicao(),
                                                                            livro_toexemplar.get_editora(),
                                                                            livro_toexemplar.get_categorias(),
                                                                            livro_toexemplar.get_numero_exemplares() + 1,
                                                                            circulacao))
                                            print(f'Exemplar cadastrado com sucesso!')
                                            input('Pressione enter para continuar...')
                                            pass

                                    case 2:
                                        print('Escolha um livro: ')
                                        conte = 0
                                        for livro in livro_dao.listar_nomes():
                                            conte += 1
                                            print(f'{conte} - {livro}')
                                        id_livro_exemplar_alterar = int(input('Digite sua opção(0 para sair): ')) - 1
                                        if id_livro_exemplar_alterar == -1:
                                            print('Saindo...')
                                            pass
                                        else:
                                            lista_exemplares = livro_dao.get_exemplares(id_livro_exemplar_alterar)
                                            contee = 1
                                            for exemplar in lista_exemplares:
                                                print(
                                                    f'{contee} - Numero: {exemplar.get_numero_exemplares()} - Circulação: {exemplar.get_circulacao()}')
                                                contee += 1
                                            escolha_exemplar = int(input('Escolha um exemplar (0 para sair): ')) - 1

                                            if escolha_exemplar == -1:
                                                print('Saindo...')
                                                pass
                                            elif escolha_exemplar > len(lista_exemplares) - 1:
                                                print('Escolha inválida!')
                                                input('Pressione enter para continuar...')
                                                pass
                                            else:
                                                print('''
                                                    Escolha o que alterar:
                                                    1 - Numero
                                                    2 - Circulação''')
                                                opcao_alterar = int(input('Digite sua opção(0 para sair): '))
                                                match opcao_alterar:
                                                    case 0:
                                                        print('Saindo...')
                                                        pass

                                                    case 1:
                                                        numero_exemplar = int(input('Insira o número do exemplar: '))
                                                        lista_exemplares[escolha_exemplar].set_numero_exemplar(
                                                            numero_exemplar)
                                                        print(
                                                            f'Número exemplar alterado com sucesso para {numero_exemplar}!')
                                                        input('Pressione enter para continuar...')

                                                    case 2:
                                                        circulacao = input(
                                                            'O exemplar poderá ser emprestado?(S/N) ').upper()
                                                        if circulacao.split()[0][0] == 'S':
                                                            circulacao = True
                                                        else:
                                                            circulacao = False
                                                        lista_exemplares[escolha_exemplar].set_circulacao(circulacao)
                                                        print(
                                                            f'Circulação do exemplar alterado com sucesso para {circulacao}')
                                                        input('Pressione enter para continuar...')

                                    case 3:
                                        print('Escolha um livro: ')
                                        conte = 0
                                        for livro in livro_dao.listar_nomes():
                                            conte += 1
                                            print(f'{conte} - {livro}')
                                        id_livro_exemplar_consultar = int(input('Digite sua opção(0 para sair): ')) - 1
                                        if id_livro_exemplar_consultar == -1:
                                            print('Saindo...')
                                            pass
                                        else:
                                            exemplares_livro = livro_dao.get_exemplares(id_livro_exemplar_consultar)
                                            contador = 0
                                            for exemplar in exemplares_livro:
                                                contador += 1
                                                print(
                                                    f'{contador} - nº{exemplar.get_numero_exemplares()} - {exemplar.get_titulo()}')
                                            input('Pressione enter para continuar...')
                                            pass

                                    case 4:

                                        print('Escolha um livro: ')
                                        conte = 0
                                        for livro in livro_dao.listar_nomes():
                                            conte += 1
                                            print(f'{conte} - {livro}')
                                        id_livro_exemplar_excluir = int(input('Digite sua opção(0 para sair): ')) - 1
                                        if id_livro_exemplar_excluir == -1:
                                            print('Saindo...')
                                            pass
                                        else:
                                            lista_exemplares = livro_dao.get_exemplares(id_livro_exemplar_excluir)
                                            contee = 1
                                            for exemplar in lista_exemplares:
                                                print(
                                                    f'{contee} - Numero: {exemplar.get_numero_exemplares()} - Circulação: {exemplar.get_circulacao()}')
                                                contee += 1
                                            escolha_exemplar = int(input('Escolha um exemplar (0 para sair): ')) - 1
                                            validacao_exemplar_excluir = input(
                                                f'Tem certeza que deseja excluir o exemplar {lista_exemplares[escolha_exemplar].get_titulo()} Numero: {lista_exemplares[escolha_exemplar].get_numero_exemplares()}?(S/N) ').upper()
                                            if validacao_exemplar_excluir.split()[0][0] == 'S':
                                                lista_exemplares.pop(escolha_exemplar)
                                                print(f'Exemplar excluido com sucesso!')
                                            else:
                                                print('Saindo...')
                                                pass
                            case 3:
                                print('''
                                    Escolha uma das opções abaixo:
                                    1 - Cadastrar Categoria
                                    2 - Alterar dados de uma Categoria
                                    3 - Consultar Dados de uma Categoria
                                    4 - Excluir uma Categoria
                                    0 - Sair''')
                                opcao_categoria = int(input('Digite sua opção(0 para sair): '))
                                match opcao_categoria:
                                    case 0:
                                        print('Saindo...')
                                        pass

                                    case 1:
                                        nome_categoria = str(input('Digite o nome da categoria: '))
                                        descricao_categoria = str(input('Digite a descrição da categoria: '))
                                        assunto_categoria = str(input('Digite o assunto da categoria: '))
                                        categoria_dao.add_categoria(
                                            Categoria(nome_categoria, descricao_categoria, assunto_categoria))
                                        print(f'Categoria {nome_categoria} cadastrada com sucesso!')
                                        input('Pressione enter para continuar...')
                                        pass

                                    case 2:
                                        print('Escolha uma categoria: ')
                                        contc = 0
                                        for categoria in categoria_dao.listar_nomes():
                                            contc += 1
                                            print(f'{contc} - {categoria}')
                                        id_categoria_alterar = int(input('Digite sua opção(0 para sair): ')) - 1
                                        if id_categoria_alterar == -1:
                                            print('Saindo...')
                                            pass
                                        else:
                                            escolha_categorias = categoria_dao.get_categoria(id_categoria_alterar)
                                            print('Escolha uma das opções abaixo: ')
                                            print(f'1 - Nome : {escolha_categorias.get_nome()}')
                                            print(f'2 - Descrição: {escolha_categorias.get_descricao()}')
                                            print(f'3 - Assunto: {escolha_categorias.get_assunto()}')
                                            opcao_alterar = int(input('Digite sua opção(0 para sair): '))
                                            match opcao_alterar:
                                                case 0:
                                                    print('Saindo...')
                                                    pass

                                                case 1:
                                                    nome_categoria = str(input('Digite o novo nome da categoria: '))
                                                    categoria_dao.alterar_nome(id_categoria_alterar, nome_categoria)
                                                    print(
                                                        f'Nome da categoria alterado com sucesso para {nome_categoria}!')
                                                    input('Pressione enter para continuar...')
                                                    pass

                                                case 2:
                                                    descricao_categoria = str(
                                                        input('Digite a nova descrição da categoria: '))
                                                    categoria_dao.alterar_descricao(id_categoria_alterar,
                                                                                    descricao_categoria)
                                                    print(
                                                        f'Descrição da categoria alterado com sucesso para {descricao_categoria}!')
                                                    input('Pressione enter para continuar...')
                                                    pass

                                                case 3:
                                                    assunto_categoria = str(
                                                        input('Digite o novo assunto da categoria: '))
                                                    categoria_dao.alterar_assunto(id_categoria_alterar,
                                                                                  assunto_categoria)
                                                    print(
                                                        f'Assunto da categoria alterado com sucesso para {assunto_categoria}!')
                                                    input('Pressione enter para continuar...')
                                                    pass

                                    case 3:
                                        print('Escolha uma categoria: ')
                                        contc = 0
                                        for categoria in categoria_dao.listar_nomes():
                                            contc += 1
                                            print(f'{contc} - {categoria}')
                                        id_categoria_alterar = int(input('Digite sua opção(0 para sair): ')) - 1
                                        if id_categoria_alterar == -1:
                                            print('Saindo...')
                                            pass
                                        else:
                                            escolha_categorias = categoria_dao.get_categoria(id_categoria_alterar)
                                            print('Escolha uma das opções abaixo: ')
                                            print(f'1 - Nome : {escolha_categorias.get_nome()}')
                                            print(f'2 - Descrição: {escolha_categorias.get_descricao()}')
                                            print(f'3 - Assunto: {escolha_categorias.get_assunto()}')
                                            input('Pressione enter para continuar...')

                                    case 4:
                                        print('Escolha uma categoria: ')
                                        contc = 0
                                        for categoria in categoria_dao.listar_nomes():
                                            contc += 1
                                            print(f'{contc} - {categoria}')
                                        id_categoria_alterar = int(input('Digite sua opção(0 para sair): ')) - 1
                                        if id_categoria_alterar == -1:
                                            print('Saindo...')
                                            pass
                                        else:
                                            escolha_categorias = categoria_dao.get_categoria(id_categoria_alterar)
                                            print(
                                                f'Tem certeza que deseja excluir a categoria {escolha_categorias.get_nome()}?')
                                            validacao_categoria_excluir = str(
                                                input('Digite S para confirmar: ')).upper()
                                            if validacao_categoria_excluir.split()[0][0] == 'S':
                                                print(
                                                    f'Categoria {escolha_categorias.get_nome()} excluida com sucesso!')
                                                categoria_dao.remover_categoria(id_categoria_alterar)
                                            else:
                                                print('Saindo...')
                                                pass
                                            input('Pressione enter para continuar...')

                            case 4:
                                pass
                case 2:  # usuario
                    while True:
                        print('''
                                Menu Usuário
                                1- Consultar Acervo
                                0- Sair''')
                        opcao_usuario = int(input('Digite sua opção: '))
                        match opcao_usuario:
                            case 1:  # cosultar acervo
                                print('Consultar Acervo')
                                busca = str(input('Digite o nome do livro, autor ou categoria que deseja cosultar: '))
                                consulta = livro_dao.consultar_acervo(busca)
                                if consulta == []:
                                    print('Nenhum livro encontrado!')
                                else:
                                    for livro in consulta:
                                        print(
                                            '----------------------------------------------------------------------------------------------------------------------')
                                        print(
                                            f'Livro: {livro.get_titulo()} - Autores: {", ".join(livro.get_autores())} - Categoria: {", ".join(livro.get_nome_categorias())} - Número de exemplares: {livro.get_numero_exemplares()}')
                                        print(
                                            '----------------------------------------------------------------------------------------------------------------------')
                                input('Pressione enter para continuar...')
                            case 0:  # sair
                                break
                case 3:  # gerente
                    while True:
                        print('''
                                Menu Gerente
                                1- Relatórios
                                2- Controlar Usuarios
                                0- Sair''')
                        opcao_gerente = int(input('Digite sua opção: '))
                        match opcao_gerente:
                            case 0:  # sair
                                print('Saindo...')
                                break
                            case 1:  # menu relatóro
                                print('''
                                Menu Relatórios
                                1- Gerar Relatório Emprestimos
                                2- Gerar Relatório Devoluções
                                3- Gerar Relatório Pendencias
                                4- Gerar Relatório Usuários
                                0- Sair''')
                                opcao_relatorios = int(input('Digite sua opção: '))
                                match opcao_relatorios:
                                    case 0:  # sair
                                        print('Saindo...')
                                        pass
                                    case 1:  # gerar relatório emprestimos
                                        print('Relatório de Emprestimos')
                                        try:
                                            emprestimo_data_inicio = input(
                                                'Informe a data de início do relatório (dd/mm/aaaa): ')
                                            emprestimo_data_fim = input(
                                                'Informe a data de fim do relatório (dd/mm/aaaa): ')
                                            emprestimos = emprestimo_dao.relatorio_emprestimos(emprestimo_data_inicio,
                                                                                               emprestimo_data_fim)
                                            if emprestimos == []:
                                                print('Nenhum empréstimo encontrado no período informado.')
                                            else:
                                                for relatorio in emprestimos:
                                                    print(
                                                        '----------------------------------------------------------------------------------------------------------------------------------------------------------')
                                                    print(
                                                        f'Emprestimo: Livro : {relatorio.get_livro()} | Exemplar: {relatorio.get_exemplar()} | Usuário: {relatorio.get_usuario()} | Data de Empréstimo: {relatorio.get_data_emprestimo()} | Data de Devolução: {relatorio.get_data_devolucao()} - Débito: {"Sim" if relatorio.get_debito() == True else "Não"}')
                                                    print(
                                                        '----------------------------------------------------------------------------------------------------------------------------------------------------------')
                                        except:
                                            print('Data inválida, favor informe novamente.')
                                        input('Pressione enter para continuar...')
                                    case 2:  # gerar relatório reservas
                                        print('Relatório de Reservas')
                                        try:
                                            reserva_data_inicio = input(
                                                'Informe a data de início da consulta (dd/mm/aaaa): ')
                                            reserva_data_fim = input('Informe a data de fim da consulta (dd/mm/aaaa): ')
                                            reservas = reserva_dao.relatorio_reservas(reserva_data_inicio,
                                                                                      reserva_data_fim)
                                            if reservas == []:
                                                print('Nenhum empréstimo encontrado no período informado.')
                                            else:
                                                for consulta in reservas:
                                                    print(
                                                        '----------------------------------------------------------------------------------------------------------------------------------------------------------')
                                                    print(
                                                        f'Reserva: Livro : {consulta.get_livro()} | Exemplar: {consulta.get_exemplar()} | Usuário: {consulta.get_usuario()} | Data de Inicio: {consulta.get_data_reserva()} | Data do Vencimento: {consulta.get_data_vencimento()} - Ativo: {"Sim" if consulta.get_ativo() else "Não"}')
                                                    print(
                                                        '----------------------------------------------------------------------------------------------------------------------------------------------------------')
                                        except:
                                            print('Data inválida, favor informe novamente.')
                                        input('Pressione enter para continuar...')
                                    case 3:  # gerar relatório pendencias
                                        print('Relatório de Pendências')
                                        try:
                                            pendencia_data_inicio = input(
                                                'Informe a data de início da consulta (dd/mm/aaaa): ')
                                            pendencia_data_fim = input(
                                                'Informe a data de fim da consulta (dd/mm/aaaa): ')
                                            pendencias = emprestimo_dao.relatorio_pendencias(pendencia_data_inicio,
                                                                                             pendencia_data_fim)
                                            if pendencias == []:
                                                print('Nenhum empréstimo encontrado no período informado.')
                                            else:
                                                for consulta in pendencias:
                                                    print(
                                                        '----------------------------------------------------------------------------------------------------------------------------------------------------------')
                                                    print(
                                                        f'Reserva: Livro : {consulta.get_livro()} | Exemplar: {consulta.get_exemplar()} | Usuário: {consulta.get_usuario()} | Data de Inicio: {consulta.get_data_emprestimo()} | Data do Vencimento: {consulta.get_data_devolucao()} - Débito: {"Sim" if consulta.get_debito() else "Não"}')
                                                    print(
                                                        '----------------------------------------------------------------------------------------------------------------------------------------------------------')
                                        except:
                                            print('Data inválida, favor informe novamente.')
                                            input('Pressione enter para continuar...')
                                    case 4:  # gerar relatório usuários
                                        print('Relatório de Usuários')
                                        for usuario in usuario_dao.listar_usuarios():
                                            print(
                                                '----------------------------------------------------------------------------------------------------------------------------------------------------------')
                                            print(
                                                f'Id: {usuario.get_id()} | Usuário: {usuario.get_nome()} | Tipo: {usuario.get_tipo()} | Debito: {"Sim" if usuario.get_debito() else "Não"} | Quantidade de Empréstimos: {usuario.get_emprestimos()}')
                                            print(
                                                '----------------------------------------------------------------------------------------------------------------------------------------------------------')
                            case 2:  # menu controlar usuários
                                print('''
                                Menu Controlar Usuários
                                1- Cadastrar Usuário
                                2- Alterar Usuário
                                3- Excluir Usuário
                                0- Sair''')
                                opcao_controlar_usuarios = int(input('Digite sua opção: '))
                                match opcao_controlar_usuarios:
                                    case 0:  # sair
                                        print('Saindo...')
                                        break
                                    case 1:  # cadastrar usuário
                                        print('Cadastrar Usuário')
                                        try:
                                            nome = input('Informe o nome do usuário: ')
                                            sobrenome = input('Informe o sobrenome do usuário: ')
                                            opcao_tipo = int(input(
                                                '1 - Aluno\n2 - Professor\n3 - Funcionário\n4 - Bibliotecário\n5 - Gerente(ADM)\nDigite sua opção: '))
                                            match opcao_tipo:
                                                case 1:  # aluno
                                                    tipo = 'Aluno'
                                                case 2:  # professor
                                                    tipo = 'Professor'
                                                case 3:  # funcionário
                                                    tipo = 'Funcionário'
                                                case 4:  # bibliotecário
                                                    tipo = 'Bibliotecário'
                                                case 5:  # gerente
                                                    tipo = 'Gerente'
                                            validacao_cadastrar_usuario = input(
                                                f'Tem certeza que deseja cadastrar o usuário {nome} {sobrenome}?(S/N) ').upper()
                                            if validacao_cadastrar_usuario.split()[0][0] == 'S':
                                                print(
                                                    f'Usuário {nome} {sobrenome} cadastrado com sucesso!')
                                                usuario_dao.cadastrar_usuario(f'{nome} {sobrenome}', tipo)
                                            else:
                                                print('Saindo...')
                                        except:
                                            print('Data inválida, favor informe novamente.')
                                        input('Pressione enter para continuar...')
                                    case 2:  # alterar usuário
                                        print('Alterar Usuário')
                                        try:
                                            cont = 0
                                            for usuario in usuario_dao.listar_nome_usuarios():
                                                cont += 1
                                                print(f'{cont} - {usuario}')
                                            id_alterar_usuario = int(input('Digite o número do usuário que deseja alterar: ')) - 1
                                            print('Opções de alteração:')
                                            print('1 - Nome/Sobrenome')
                                            print('2 - Tipo')
                                            opcao_alterar_usuario = int(input('Digite sua opção: '))
                                            match opcao_alterar_usuario:
                                                case 1:  # alterar nome/sobrenome
                                                    try:
                                                        print(f'Informe o novo nome/sobrenome do usuário {usuario_dao.get_nome_usuario(id_alterar_usuario)}: ')
                                                        nome = input('Informe o nome do usuário: ')
                                                        sobrenome = input('Informe o sobrenome do usuário: ')
                                                        validacao_alterar_usuario = input(
                                                            f'Tem certeza que deseja alterar o usuário {usuario_dao.get_nome_usuario(id_alterar_usuario)} para {nome} {sobrenome}?(S/N) ').upper()
                                                        if validacao_alterar_usuario.split()[0][0] == 'S':
                                                            print(
                                                                f'Usuário {usuario_dao.get_nome_usuario(id_alterar_usuario)} alterado com sucesso!')
                                                            usuario_dao.alterar_nome_usuario(id_alterar_usuario, f'{nome} {sobrenome}')
                                                        else:
                                                            print('Saindo...')
                                                    except:
                                                        print('Data inválida, favor informe novamente.')
                                                case 2:  # alterar tipo
                                                    try:
                                                        opcao_tipo = int(input(
                                                            '1 - Aluno\n2 - Professor\n3 - Funcionário\n4 - Bibliotecário\n5 - Gerente(ADM)\nDigite sua opção: '))
                                                        match opcao_tipo:
                                                            case 1:  # aluno
                                                                tipo = 'Aluno'
                                                            case 2:  # professor
                                                                tipo = 'Professor'
                                                            case 3:  # funcionário
                                                                tipo = 'Funcionário'
                                                            case 4:  # bibliotecário
                                                                tipo = 'Bibliotecário'
                                                            case 5:  # gerente
                                                                tipo = 'Gerente'
                                                        validacao_alterar_usuario = input(
                                                            f'Tem certeza que deseja alterar o usuário {usuario_dao.get_nome_usuario(id_alterar_usuario)} para {tipo}?(S/N) ').upper()
                                                        if validacao_alterar_usuario.split()[0][0] == 'S':
                                                            print(
                                                                f'Usuário {usuario_dao.get_nome_usuario(id_alterar_usuario)} alterado com sucesso!')
                                                            usuario_dao.alterar_tipo_usuario(id_alterar_usuario, tipo)
                                                        else:
                                                            print('Saindo...')
                                                    except:
                                                        print('Data inválida, favor informe novamente.')
                                        except:
                                            print('Data inválida, favor informe novamente.')
                                        input('Pressione enter para continuar...')
                                    case 3:  # excluir usuário
                                        print('Excluir Usuário')
                                        try:
                                            cont = 0
                                            for usuario in usuario_dao.listar_nome_usuarios():
                                                cont += 1
                                                print(f'{cont} - {usuario}')
                                            id_excluir_usuario = int(input('Digite o número do usuário que deseja excluir: ')) - 1
                                            validacao_excluir_usuario = input(
                                                f'Tem certeza que deseja excluir o usuário {usuario_dao.get_nome_usuario(id_excluir_usuario)}?(S/N) ').upper()
                                            if validacao_excluir_usuario.split()[0][0] == 'S':
                                                print(
                                                    f'Usuário {usuario_dao.get_nome_usuario(id_excluir_usuario)} excluído com sucesso!')
                                                usuario_dao.excluir_usuario(id_excluir_usuario)
                                            else:
                                                print('Saindo...')
                                        except:
                                            print('Data inválida, favor informe novamente.')
                                        input('Pressione enter para continuar...')
                case 4:  # funcionario
                    while True:
                        print('''
                                Menu Funcionário
                                1- Controle de Empréstimos
                                2- Controle de Reserva
                                0 - Sair''')
                        menu_funcionario = int(input('Digite sua opção: '))
                        match menu_funcionario:
                            case 0:
                                print('Saindo...')
                                break
                            case 1:  # empréstimo
                                print('''
                                    Menu Emprestimo
                                    1- Novo Empréstimo
                                    2- Consultar Empréstimos
                                    3- Devolução
                                    0 - Sair''')
                                menu_emprestimo = int(input('Digite sua opção: '))
                                match menu_emprestimo:
                                    case 0:
                                        print('Saindo...')
                                        pass
                                    case 1:  # novo empréstimo
                                        print('Novo Empréstimo')
                                        usuario_id_emprestimo = int(input('Digite o ID do usuário: '))
                                        cont = 0
                                        for livro in livro_dao.listar_nomes():
                                            cont += 1
                                            print(f'{cont} - {livro}')
                                        livro_id_emprestimo = int(input('Digite sua opção(0 para sair): ')) - 1
                                        if livro_id_emprestimo == -1:
                                            print('Saindo...')
                                            pass
                                        else:
                                            cont_exemp = 0
                                            for exemplar in livro_dao.get_exemplares(livro_id_emprestimo):
                                                cont_exemp += 1
                                                print(
                                                    f'{cont_exemp} - {exemplar.get_titulo()} - Circulação: {"10 dias corridos" if exemplar.get_circulacao() else "1 dia útil"} - '
                                                    f'Emprestimo: {"Emprestado" if exemplar.get_emprestimo() else "Não Emprestado"} - Reserva: {"Reservado" if exemplar.is_reservado() else "Não Reservado"}')
                                            exemplar_id_emprestimo = int(input('Digite sua opção(0 para sair): ')) - 1
                                            if exemplar_id_emprestimo == -1:
                                                print('Saindo...')
                                                pass
                                            else:
                                                print(emprestimo_dao.novo_emprestimo(usuario_id_emprestimo,
                                                                                     livro_id_emprestimo,
                                                                                     exemplar_id_emprestimo))
                                                input('Pressione enter para continuar...')
                                    case 2:  # consultar empréstimos
                                        print('Consultar Empréstimos')
                                        try:
                                            consulta_data_inicio = input(
                                                'Informe a data de início da consulta (dd/mm/aaaa): ')
                                            consulta_data_fim = input(
                                                'Informe a data de fim da consulta (dd/mm/aaaa): ')
                                            consultas = emprestimo_dao.relatorio_emprestimos(consulta_data_inicio,
                                                                                             consulta_data_fim)
                                            if consultas == []:
                                                print('Nenhum empréstimo encontrado no período informado.')
                                            else:
                                                for consulta in consultas:
                                                    print(
                                                        '----------------------------------------------------------------------------------------------------------------------------------------------------------')
                                                    print(
                                                        f'Emprestimo: Livro : {consulta.get_livro()} | Exemplar: {consulta.get_exemplar()} | Usuário: {consulta.get_usuario()} | Data de Empréstimo: {consulta.get_data_emprestimo()} | Data de Devolução: {consulta.get_data_devolucao()} - Débito: {"Sim" if consulta.get_debito() == True else "Não"}')
                                                    print(
                                                        '----------------------------------------------------------------------------------------------------------------------------------------------------------')
                                        except:
                                            print('Data inválida, favor informe novamente.')
                                        input('Pressione enter para continuar...')
                                    case 3:  # devolução
                                        print('Devolução')
                                        emprestimo_id_devolucao = int(input('Digite o ID do usuário: '))
                                        pendencias = emprestimo_dao.pendencias_emprestimo(emprestimo_id_devolucao)
                                        if pendencias == []:
                                            print('Nenhuma pendência encontrada.')
                                        else:
                                            for pendencia in pendencias:
                                                print(
                                                    '----------------------------------------------------------------------------------------------------------------------------------------------------------')
                                                print(
                                                    f'{pendencias.index(pendencia) + 1} - Livro: {pendencia.get_livro()} - Exemplar: {pendencia.get_exemplar()} - Usuário: {pendencia.get_usuario()} - Data de Empréstimo: {pendencia.get_data_emprestimo()} - Data de Devolução: {pendencia.get_data_devolucao()} - Débito: {"Sim" if pendencia.get_debito() == True else "Não"}')
                                                print(
                                                    '----------------------------------------------------------------------------------------------------------------------------------------------------------')
                                            select_pendencia = (int(input(
                                                'Digite o número da pendência deseja devolver: ')) - 1)
                                            id_pendencia = pendencias[select_pendencia].get_id()
                                            print(emprestimo_dao.devolucao_emprestimo(id_pendencia))
                                            input('Pressione enter para continuar...')
                            case 2:  # reserva
                                print('''
                                    Menu Reserva
                                    1- Nova Reserva
                                    2- Consultar Reservas
                                    3- Cancelar Reserva
                                    0 - Sair''')
                                menu_reserva = int(input('Digite sua opção: '))
                                match menu_reserva:
                                    case 0:  # sair
                                        print('Saindo...')
                                        pass
                                    case 1:  # nova reserva
                                        print('Nova Reserva')
                                        usuario_id_reserva = int(input('Digite o ID do usuário: '))
                                        cont = 0
                                        for livro in livro_dao.listar_nomes():
                                            cont += 1
                                            print(f'{cont} - {livro}')
                                        livro_id_reserva = int(input('Digite sua opção(0 para sair): ')) - 1
                                        if livro_id_reserva == -1:
                                            print('Saindo...')
                                            pass
                                        else:
                                            cont_exemp = 0
                                            for exemplar in livro_dao.get_exemplares(livro_id_reserva):
                                                cont_exemp += 1
                                                print(
                                                    f'{cont_exemp} - {exemplar.get_titulo()} - Circulação: {"10 dias corridos" if exemplar.get_circulacao() else "NÃO PODE SER RESERVADO"} - '
                                                    f'Emprestimo: {"Emprestado" if exemplar.get_emprestimo() else "Não Emprestado"} - Reserva: {"Reservado" if exemplar.is_reservado() else "Não Reservado"}')
                                            exemplar_id_reserva = int(input('Digite sua opção(0 para sair): ')) - 1
                                            if exemplar_id_reserva == -1:
                                                print('Saindo...')
                                                pass
                                            else:
                                                print(reserva_dao.nova_reserva(usuario_id_reserva, livro_id_reserva,
                                                                               exemplar_id_reserva))
                                                input('Pressione enter para continuar...')
                                    case 2:  # consultar reservas
                                        print('Consultar Reservas')
                                        try:
                                            consulta_data_inicio = input(
                                                'Informe a data de início da consulta (dd/mm/aaaa): ')
                                            consulta_data_fim = input(
                                                'Informe a data de fim da consulta (dd/mm/aaaa): ')
                                            consultas = reserva_dao.relatorio_reservas(consulta_data_inicio,
                                                                                       consulta_data_fim)
                                            if consultas == []:
                                                print('Nenhum empréstimo encontrado no período informado.')
                                            else:
                                                for consulta in consultas:
                                                    print(
                                                        '----------------------------------------------------------------------------------------------------------------------------------------------------------')
                                                    print(
                                                        f'Reserva: Livro : {consulta.get_livro()} | Exemplar: {consulta.get_exemplar()} | Usuário: {consulta.get_usuario()} | Data de Inicio: {consulta.get_data_reserva()} | Data do Vencimento: {consulta.get_data_vencimento()} - Ativo: {"Sim" if consulta.get_ativo() else "Não"}')
                                                    print(
                                                        '----------------------------------------------------------------------------------------------------------------------------------------------------------')
                                        except:
                                            print('Data inválida, favor informe novamente.')
                                        input('Pressione enter para continuar...')
                                    case 3:  # cancelar reserva
                                        print('Devolução')
                                        reserva_id_devolucao = int(input('Digite o ID do usuário: '))
                                        pendencias = reserva_dao.pendencias_reserva(reserva_id_devolucao)
                                        if pendencias == []:
                                            print('Nenhuma pendência encontrada.')
                                        else:
                                            for pendencia in pendencias:
                                                print(
                                                    '----------------------------------------------------------------------------------------------------------------------------------------------------------')
                                                print(
                                                    f'{pendencias.index(pendencia) + 1} - Livro: {pendencia.get_livro()} - Exemplar: {pendencia.get_exemplar()} - Usuário: {pendencia.get_usuario()} - Data de Empréstimo: {pendencia.get_data_reserva()} - Data de Devolução: {pendencia.get_data_vencimento()} - Ativo: {"Sim" if pendencia.get_ativo() else "Não"}')
                                                print(
                                                    '----------------------------------------------------------------------------------------------------------------------------------------------------------')
                                            select_pendencia = (int(input(
                                                'Digite o número da pendência deseja devolver: ')) - 1)
                                            id_pendencia = pendencias[select_pendencia].get_id()
                                            print(reserva_dao.cancelamento_reserva(id_pendencia))
                                            input('Pressione enter para continuar...')

    except ValueError:
        print('Valor invalido')
