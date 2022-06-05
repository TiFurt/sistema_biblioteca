from model.dao.data import usuarios
from datetime import date

from model.entity.usuario import Usuario


class UsuarioDao:

    def __init__(self) -> None:
        pass

    def listar_usuarios(self):
        return usuarios

    def cadastrar_usuario(self, nomeSobrenome, tipo) -> None:
        id = len(usuarios) + 1
        usuarios.append(Usuario(id, nomeSobrenome, tipo))

    def listar_nome_usuarios(self) -> list:
        return [usuario.get_nome() for usuario in usuarios]

    def get_nome_usuario(self, id) -> str:
        return usuarios[id].get_nome()

    def alterar_nome_usuario(self, id, nomeSobrenome) -> None:
        usuarios[id].set_nome(nomeSobrenome)

    def alterar_tipo_usuario(self, id, tipo) -> None:
        usuarios[id].set_tipo(tipo)

    def get_tipo_usuario(self, id) -> str:
        return usuarios[id].get_tipo()

    def excluir_usuario(self, id) -> None:
        usuarios.pop(id)
