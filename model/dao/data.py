from model.entity.livro import Livro
from model.entity.exemplar import Exemplar
from model.entity.categoria import Categoria
from model.entity.emprestimo import Emprestimo
from model.entity.usuario import Usuario


livros = [
    Livro('Clean Code', ['Robert C. Martin'], 2008, '0132350882', '1ª edição', 'Prentice Hall', [Categoria('Programação', 'Programação é um gênero literário que se caracteriza por serem livros que contêm o conteúdo de programação.', 'Livro de programação'),]),
    Livro('O Pequeno Princepe', ['Antoine de Saint-Exupéry'], 1843, '9788596516097', '1ª edição', 'Editora Abril', [Categoria('Fantasia', 'Fantasia é um gênero literário que se caracteriza por serem livros que contêm contos de fantasia.', 'Livro de fantasia'),]),
    Livro('Diario de um Banana', ['José Saramago'], 1892, '9788596516097', '1ª edição', 'Editora Abril', [Categoria('Sci-Fi', 'Sci-Fi é um gênero literário que se caracteriza por serem livros que contêm contos de ficção científica.', 'Livro de ficção científica'),]),
    Livro('Inferno', ['Dan Brown'], 2005, '9788596516097', '1ª edição', 'Editora Abril', [Categoria('Ficção', 'Ficção é um gênero literário que se caracteriza por serem livros que contêm contos de ficção.', 'Livro de ficção'),]),
    Livro('Iracema', ['Machado de Assis'], 1828, '9788596516097', '1ª edição', 'Editora Abril', [Categoria('Ficção', 'Ficção é um gênero literário que se caracteriza por serem livros que contêm contos de ficção.', 'Livro de ficção'),]),
]



exemplares = [
    Exemplar('Clean Code', ['Robert C. Martin'], 2008, '0132350882', '1ª edição', 'Prentice Hall', [Categoria('Programação', 'Programação é um gênero literário que se caracteriza por serem livros que contêm o conteúdo de programação.', 'Livro de programação'),], 1, False, False, False),
    Exemplar('Clean Code', ['Robert C. Martin'], 2008, '0132350882', '1ª edição', 'Prentice Hall', [Categoria('Programação', 'Programação é um gênero literário que se caracteriza por serem livros que contêm o conteúdo de programação.', 'Livro de programação'),], 2, False, False, False),
    Exemplar('O Pequeno Princepe', ['Antoine de Saint-Exupéry'], 1843, '9788596516097', '1ª edição', 'Editora Abril', [Categoria('Fantasia', 'Fantasia é um gênero literário que se caracteriza por serem livros que contêm contos de fantasia.', 'Livro de fantasia')], 3, False, False, False),
    Exemplar('Diario de um Banana', ['José Saramago'], 1892, '9788596516097', '1ª edição', 'Editora Abril', [Categoria('Sci-Fi', 'Sci-Fi é um gênero literário que se caracteriza por serem livros que contêm contos de ficção científica.', 'Livro de ficção científica')], 4, True, False, False),
    Exemplar('Inferno', ['Dan Brown'], 2005, '9788596516097', '1ª edição', 'Editora Abril', [Categoria('Ficção', 'Ficção é um gênero literário que se caracteriza por serem livros que contêm contos de ficção.', 'Livro de ficção'),], 5, True, False, False),
    Exemplar('Inferno', ['Dan Brown'], 2005, '9788596516097', '1ª edição', 'Editora Abril', [Categoria('Ficção', 'Ficção é um gênero literário que se caracteriza por serem livros que contêm contos de ficção.', 'Livro de ficção'),], 6, False, False, False),
]

categorias = [
    Categoria('Ficção', 'Ficção é um gênero literário que se caracteriza por serem livros que contêm contos de ficção.', 'Livro de ficção'),
    Categoria('Fantasia', 'Fantasia é um gênero literário que se caracteriza por serem livros que contêm contos de fantasia.', 'Livro de fantasia'),
    Categoria('Sci-Fi', 'Sci-Fi é um gênero literário que se caracteriza por serem livros que contêm contos de ficção científica.', 'Livro de ficção científica'),
    Categoria('Programação', 'Programação é um gênero literário que se caracteriza por serem livros que contêm o conteúdo de programação.', 'Livro de programação'),
]


for exemplar in exemplares:
    for livro in livros:
        if exemplar.get_titulo() == livro.get_titulo():
            livro.add_exemplar(exemplar)


emprestimos =[
    Emprestimo('Clean Code', 1, '20/03/2022', '21/03/2022', False, '001'),
]

tipos_usuario =[
    'funcionario',
    'aluno',
    'professor'
]

usuarios =[
    Usuario(1, 'João', 'funcionario', False, 0),
    Usuario(2, 'Maria', 'aluno', False, 0),
    Usuario(3, 'Tassio', 'professor', False, 0),
]