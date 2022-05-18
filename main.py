from model.dao.livro_dao import LivroDao
from model.entity.livro import Livro
from model.dao.exemplar_dao import ExemplarDao
from model.entity.exemplar import Exemplar


if __name__ == '__main__':
    livro_dao = LivroDao()
    exemplar_dao = ExemplarDao()
    try:
        while True:
            print('''
Escolha uma das opções abaixo:
1 - Livros
2 - Exemplares
3 - Consultar Acervo
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
                            assuntos = []
                            while True:
                                assunto = input('insira os assuntos do livro (0 para continuar): ')
                                if assunto == '0':
                                    break
                                assuntos.append(assunto)

                            livro_dao.add_livro(Livro(titulo, autores, ano, isbn, edicao, editora, assuntos))
                            print(f'Livro {titulo} cadastrado com sucesso!')
                            pass
                        
                        case 2:
                            print('Escolha um livro para alterar: ')
                            cont = 0
                            for livro in livro_dao.listar_nomes():
                                cont += 1
                                print(f'{cont} - {livro}')
                            escolha_livro = int(input('Digite sua opção: ')) - 1
                            livro = livro_dao.listar_livros()[escolha_livro]
                            print(f'''
1- Titulo: {livro.get_titulo()}
2- Autor: {', '.join(livro.get_autores())}
3- Ano: {livro.get_ano()}
4- ISBN: {livro.get_isbn()}
5- Edicao: {livro.get_edicao()}
6- Editora: {livro.get_editora()}
7- Assuntos: {', '.join(livro.get_assuntos())}
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
                                    assuntos_alteracao = []
                                    while True:
                                        assunto_alteracao = input('Insira os autores do livro(0 para continuar): ')
                                        if assunto_alteracao == '0':
                                            break
                                        assuntos_alteracao.append(assunto_alteracao)
                                    livro_dao.alterar_assuntos(escolha_livro, assuntos_alteracao)
                                    print(f'Assuntos alterados para {", ".join(assuntos_alteracao)}')
                            pass
                        
                        case 3:
                            print('Escolha um livro para consultar: ')
                            contc = 0
                            for livro in livro_dao.listar_nomes():
                                contc += 1
                                print(f'{contc} - {livro}')
                            escolha_consulta = int(input('Digite sua opção(0 para sair): ')) - 1
                            if escolha_consulta == 0:
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
Assuntos: {', '.join(consulta.get_assuntos())}
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
                                livro_dao.add_exemplar(id_livro_cadastrar, Exemplar(livro_toexemplar.get_titulo(), livro_toexemplar.get_autores(), livro_toexemplar.get_ano(), livro_toexemplar.get_isbn(), livro_toexemplar.get_edicao(), livro_toexemplar.get_editora(), livro_toexemplar.get_assuntos(), livro_toexemplar.get_numero_exemplar(), circulacao))
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
                                    print(f'{contee} - Numero: {exemplar.get_numero_exemplar()} - Circulação: {exemplar.get_circulacao()}')
                                    contee += 1
                                escolha_exemplar = int(input('Escolha um exemplar (0 para sair): ')) -1
                                
                                if escolha_exemplar == -1:
                                    print('Saindo...')
                                    pass
                                elif escolha_exemplar > len(lista_exemplares) -1:
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
                                    print(f'{contador} - nº{exemplar.get_numero_exemplar()} - {exemplar.get_titulo()}')
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
                                    print(f'{contee} - Numero: {exemplar.get_numero_exemplar()} - Circulação: {exemplar.get_circulacao()}')
                                    contee += 1
                                escolha_exemplar = int(input('Escolha um exemplar (0 para sair): ')) -1
                                validacao_exemplar_excluir = input(f'Tem certeza que deseja excluir o exemplar {lista_exemplares[escolha_exemplar].get_titulo()} Numero: {exemplar.get_numero_exemplar()}?(S/N) ').upper()
                                if validacao_exemplar_excluir.split()[0][0] == 'S': 
                                        lista_exemplares.pop(escolha_exemplar)
                                        print(f'Exemplar excluido com sucesso!')
                                else:
                                    print('Saindo...')
                                    pass

    except ValueError:
        print('Valor invalido')
