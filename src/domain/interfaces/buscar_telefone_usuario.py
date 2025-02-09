from abc import ABC, abstractmethod


class BuscarTelefoneUsuario(ABC):
    @abstractmethod
    def obter_telefone_usuario(self, nome_usuario):
        pass
