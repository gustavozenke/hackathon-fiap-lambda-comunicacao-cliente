from abc import ABC, abstractmethod


class NotificacaoUseCaseInterface(ABC):
    @abstractmethod
    def enviar_notificacao(self, nome_usuario: str, message: str):
        pass
