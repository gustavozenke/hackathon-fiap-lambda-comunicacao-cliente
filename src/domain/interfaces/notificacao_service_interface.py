from abc import ABC, abstractmethod


class NotificacaoServiceInterface(ABC):
    @abstractmethod
    def notificar(self, nome_usuario: str, message: str):
        pass
