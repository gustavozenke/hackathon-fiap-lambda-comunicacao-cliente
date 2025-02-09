from abc import ABC, abstractmethod


class Notificacao(ABC):
    @abstractmethod
    def notificar(self, nome_usuario: str, message: str):
        pass
