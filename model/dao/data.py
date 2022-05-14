from model.entity.livro import Livro
from model.entity.exemplar import Exemplar


livros = [
    Livro('O Poder do Hipernótico', ['José Saramago'], 1892, '9788596516097', '1ª edição', 'Editora Abril', ['Ficção', 'Fantasia', 'Sci-Fi']),
    Livro('Clean Code', ['Robert C. Martin'], 2008, '0132350882', '1ª edição', 'Prentice Hall', ['Programação']),
    Livro('O Pequeno Princepe', ['Antoine de Saint-Exupéry'], 1843, '9788596516097', '1ª edição', 'Editora Abril', ['Ficção', 'Fantasia', 'Sci-Fi']),
    Livro('Diario de um Banana', ['José Saramago'], 1892, '9788596516097', '1ª edição', 'Editora Abril', ['Ficção', 'Fantasia', 'Sci-Fi']),
    Livro('Inferno', ['Dan Brown'], 2005, '9788596516097', '1ª edição', 'Editora Abril', ['Ficção', 'Fantasia', 'Sci-Fi']),
    Livro('Iracema', ['Machado de Assis'], 1828, '9788596516097', '1ª edição', 'Editora Abril', ['Ficção', 'Fantasia', 'Sci-Fi']),
]



exemplares = [
    Exemplar('O Poder do Hipernótico', ['José Saramago'], 1892, '9788596516097', '1ª edição', 'Editora Abril', ['Ficção', 'Fantasia', 'Sci-Fi'], 1, 'Não'),
    Exemplar('Clean Code', ['Robert C. Martin'], 2008, '0132350882', '1ª edição', 'Prentice Hall', ['Programação'], 2, 'Não'),
    Exemplar('O Pequeno Princepe', ['Antoine de Saint-Exupéry'], 1843, '9788596516097', '1ª edição', 'Editora Abril', ['Ficção', 'Fantasia', 'Sci-Fi'], 3, 'Não'),
    Exemplar('Diario de um Banana', ['José Saramago'], 1892, '9788596516097', '1ª edição', 'Editora Abril', ['Ficção', 'Fantasia', 'Sci-Fi'], 4, 'Não'),
    Exemplar('Inferno', ['Dan Brown'], 2005, '9788596516097', '1ª edição', 'Editora Abril', ['Ficção', 'Fantasia', 'Sci-Fi'], 5, 'Não'),
    Exemplar('Inferno', ['Dan Brown'], 2005, '9788596516097', '1ª edição', 'Editora Abril', ['Ficção', 'Fantasia', 'Sci-Fi'], 6, 'Não'),
]

for exemplar in exemplares:
    for livro in livros:
        if exemplar.get_titulo() == livro.get_titulo():
            livro.add_exemplar(exemplar)


