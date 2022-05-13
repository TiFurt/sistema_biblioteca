from model.dao.livro_dao import LivroDao
from model.entity.livro import Livro
# from model.dao.exemplar_dao import ExemplarDao


if __name__ == '__main__':
    livro_dao = LivroDao()
    try:
        while True:
                print ('''Escolha uma das opções abaixo:
                        1 - Livros
                        2 - Exemplares
                        3 - Consultar Acervo
                        0 - Sair''')
                opcao = int(input('Digite sua opção(0 para sair): '))
                match opcao:
                    case 0:
                        print('Saindo...')
                        break                    
                    case 1:
                        print ('''Escolha uma das opções abaixo:
                                1 - Cadastrar Livros
                                2 - Alterar dados  de um Livro
                                3 - Consultar Dados de um Livro
                                4 - Excluir um Livro
                                0 - Sair''')
                        opcao = int(input('Digite sua opção(0 para sair): '))
                        match opcao:
                            case 0:
                                print('Saindo...')
                                pass
                            case 1:
                                titulo = input('Insira o título do livro: ')
                                autor = input('Insira o autor do livro: ')
                                ano = input('Insira o ano de publicação do livro: ')
                                isbn = input('Insira o ISBN do livro: ')
                                edicao = input('Insira a edição do livro: ')
                                editora = input('Insira a editora do livro: ')
                                assuntos = input('insira os assuntos do livro: ')
                                livro_dao.add_livro(Livro(titulo, autor, ano, isbn, edicao, editora, assuntos))
                                print(f'Livro {titulo} cadastrado com sucesso!')
                                pass
                            case 2:
                                print('Escolha um livro para alterar: ')
                                cont = 0
                                for livro in livro_dao.listar_nomes():
                                    cont += 1
                                    print(f'{cont} - {livro}')
                                opcao = int(input('Digite sua opção: '))
                                livro = livro_dao.listar_livros()[opcao - 1]
                                print(f'''
                                        1- Titulo: {livro.get_titulo()}
                                        2- Autor: {[autor for autor in livro.get_autores()]}
                                        3- Ano: {livro.get_ano()}
                                        4- ISBN: {livro.get_isbn()}
                                        5- Edicao: {livro.get_edicao()}
                                        6- Editora: {livro.get_editora()}
                                        7- Assuntos: {livro.get_assuntos()}
                                        0- Sair''')
                                pass
                            case 3:
                                print('Escolha um livro para consultar: ')
                                pass
                        
                    


    except ValueError:
        print('Valor invalido')