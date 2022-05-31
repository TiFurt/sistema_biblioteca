from model.dao.livro_dao import LivroDao
from model.dao.exemplar_dao import ExemplarDao
from model.dao.categoria_dao import CategoriaDao
from model.entity.livro import Livro
from model.entity.exemplar import Exemplar
from model.entity.categoria import Categoria

if __name__ == '__main__':
    livro_dao = LivroDao()
    exemplar_dao = ExemplarDao()
    categoria_dao = CategoriaDao()

    try:
        while True:
            print('''
                Escolha uma das opções abaixo:
                1 - Livros
                2 - Exemplares
                3 - Categorias
                4 - Consultar Acervo
                0 - Sair''')
            opcao_menu = int(input('Digite sua opção(0 para sair): '))
            match opcao_menu:
                case 0:
                    print('Saindo...')
                    break
                case 1:
                    print('''
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
                                id_categoria_adicionar_livro = int(input('Escolha a categoria (0 para continuar): ')) -1
                                if id_categoria_adicionar_livro == -1:
                                    break
                                elif categoria_dao.get_categoria(id_categoria_adicionar_livro) in categorias:
                                    print('Categoria já adicionada!')
                                    input('Pressione enter para continuar...')
                                else:
                                    categorias.append(categoria_dao.get_categoria(id_categoria_adicionar_livro))
                                    print(f'Categoria {categoria_dao.get_nome(id_categoria_adicionar_livro)} adicionada com sucesso!')
                                
                            livro_dao.add_livro(Livro(titulo, autores, ano, isbn, edicao, editora, categorias))
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
                                        autor_alteracao = input('Insira os autores do livro(0 para continuar): ')
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
                                        id_alterar_categoria_livro = int(input('Escolha a categoria (0 para continuar): ')) -1
                                        if id_alterar_categoria_livro == -1:
                                            break
                                        elif categoria_dao.get_categoria(id_alterar_categoria_livro) in categorias:
                                            print('Categoria já adicionada!')
                                            input('Pressione enter para continuar...')
                                        else:
                                            categorias.append(categoria_dao.get_categoria(id_alterar_categoria_livro))
                                            print(f'Categoria {categoria_dao.get_nome(id_alterar_categoria_livro)} adicionada com sucesso!')
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
                                        print(f'Livro {livro_dao.get_titulo(id_livro_excluir)} excluido com sucesso!')
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
                                livro_dao.add_exemplar(id_livro_cadastrar, Exemplar(livro_toexemplar.get_titulo(),
                                                                                    livro_toexemplar.get_autores(),
                                                                                    livro_toexemplar.get_ano(),
                                                                                    livro_toexemplar.get_isbn(),
                                                                                    livro_toexemplar.get_edicao(),
                                                                                    livro_toexemplar.get_editora(),
                                                                                    livro_toexemplar.get_categorias(),
                                                                                    livro_toexemplar.get_numero_exemplares(),
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
                                            lista_exemplares[escolha_exemplar].set_numero_exemplar(numero_exemplar)
                                            print(f'Número exemplar alterado com sucesso para {numero_exemplar}!')
                                            input('Pressione enter para continuar...')

                                        case 2:
                                            circulacao = input('O exemplar poderá ser emprestado?(S/N) ').upper()
                                            if circulacao.split()[0][0] == 'S':
                                                circulacao = True
                                            else:
                                                circulacao = False
                                            lista_exemplares[escolha_exemplar].set_circulacao(circulacao)
                                            print(f'Circulação do exemplar alterado com sucesso para {circulacao}')
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
                                    print(f'{contador} - nº{exemplar.get_numero_exemplares()} - {exemplar.get_titulo()}')
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
                                lista_exemplares = livro_dao.get_exemplares(id_livro_exemplar_alterar)
                                contee = 1
                                for exemplar in lista_exemplares:
                                    print(
                                        f'{contee} - Numero: {exemplar.get_numero_exemplares()} - Circulação: {exemplar.get_circulacao()}')
                                    contee += 1
                                escolha_exemplar = int(input('Escolha um exemplar (0 para sair): ')) - 1
                                validacao_exemplar_excluir = input(
                                    f'Tem certeza que deseja excluir o exemplar {lista_exemplares[escolha_exemplar].get_titulo()} Numero: {exemplar.get_numero_exemplares()}?(S/N) ').upper()
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
                            categoria_dao.add_categoria(Categoria(nome_categoria, descricao_categoria, assunto_categoria))
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
                                        print(f'Nome da categoria alterado com sucesso para {nome_categoria}!')
                                        input('Pressione enter para continuar...')
                                        pass

                                    case 2:
                                        descricao_categoria = str(input('Digite a nova descrição da categoria: '))
                                        categoria_dao.alterar_descricao(id_categoria_alterar, descricao_categoria)
                                        print(
                                            f'Descrição da categoria alterado com sucesso para {descricao_categoria}!')
                                        input('Pressione enter para continuar...')
                                        pass

                                    case 3:
                                        assunto_categoria = str(input('Digite o novo assunto da categoria: '))
                                        categoria_dao.alterar_assunto(id_categoria_alterar, assunto_categoria)
                                        print(f'Assunto da categoria alterado com sucesso para {assunto_categoria}!')
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
                                print(f'Tem certeza que deseja excluir a categoria {escolha_categorias.get_nome()}?')
                                validacao_categoria_excluir = str(input('Digite S para confirmar: ')).upper()
                                if validacao_categoria_excluir.split()[0][0] == 'S':
                                    print(f'Categoria {escolha_categorias.get_nome()} excluida com sucesso!')
                                    categoria_dao.remover_categoria(id_categoria_alterar)
                                else:
                                    print('Saindo...')
                                    pass
                                input('Pressione enter para continuar...')
                case 4:
                    #cosultar acervo
                    print('Consultar Acervo')
                    busca = str(input('Digite o nome do livro, autor ou categoria que deseja cosultar: '))
                    consulta = livro_dao.consultar_acervo(busca)
                    if consulta == []:
                        print('Nenhum livro encontrado!')
                    else:
                        for livro in consulta:
                            print('----------------------------------------------------------------------------------------------------------------------')
                            print(f'Livro: {livro.get_titulo()} - Autores: {", ".join(livro.get_autores())} - Categoria: {", ".join(livro.get_nome_categorias())} - Número de exemplares: {livro.get_numero_exemplares()}')
                        print('----------------------------------------------------------------------------------------------------------------------')
                    input('Pressione enter para continuar...')

                case 5:
                    pass






    except ValueError:
        print('Valor invalido')
