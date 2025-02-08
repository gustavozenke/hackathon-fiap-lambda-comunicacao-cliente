from abc import ABC, abstractmethod


class NotificacaoInterface(ABC):
    @abstractmethod
    def enviar_notificacao(self, to_address: str, nome_usuario: str, message: str):
        pass
