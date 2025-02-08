from botocore.exceptions import ClientError

from domain.interfaces.buscar_telefone_usuario_usecase_interface import BuscarTelefoneUsuarioUseCaseInterface
from utils.utils import inserir_pais_telefone


class BuscarTelefoneUsuarioUseCase(BuscarTelefoneUsuarioUseCaseInterface):

    def __init__(self, cognito_repository):
        self.cognito_repository = cognito_repository

    def obter_telefone_usuario(self, nome_usuario):
        try:
            response = self.cognito_repository.admin_get_user(nome_usuario)
            for attribute in response['UserAttributes']:
                if attribute['Name'] == 'phone_number':
                    return inserir_pais_telefone(attribute['Value'])
            return None
        except ClientError as e:
            print(f"Erro ao buscar o usuário: {e}")
            return None
