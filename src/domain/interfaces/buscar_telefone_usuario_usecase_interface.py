from abc import ABC, abstractmethod


class BuscarTelefoneUsuarioUseCaseInterface(ABC):
    @abstractmethod
    def obter_telefone_usuario(self, nome_usuario):
        pass
