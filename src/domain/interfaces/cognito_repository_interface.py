from abc import abstractmethod, ABC


class CognitoRepositoryInterface(ABC):
    @abstractmethod
    def admin_get_user(self, nome_usuario):
        pass
