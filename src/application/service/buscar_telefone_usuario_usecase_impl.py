import logging

from botocore.exceptions import ClientError

from domain.interfaces.buscar_telefone_usuario import BuscarTelefoneUsuario
from domain.interfaces.cognito_repository import CognitoRepository
from utils.utils import inserir_prefixo_codigo_pais

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BuscarTelefoneUsuarioUseCaseImpl(BuscarTelefoneUsuario):

    def __init__(self, cognito_repository: CognitoRepository):
        self.cognito_repository = cognito_repository

    def obter_telefone_usuario(self, nome_usuario):
        try:
            logger.info(f"Consultando numero de telefone do usuario {nome_usuario}")
            response = self.cognito_repository.admin_get_user(nome_usuario)
            for attribute in response['UserAttributes']:
                if attribute['Name'] == 'phone_number':
                    telefone = inserir_prefixo_codigo_pais(attribute['Value'])
                    logger.info(f"Telefone do usuario {nome_usuario} obtido com sucesso. Telefone={telefone}")
                    return telefone
            return None
        except ClientError as erro:
            logger.error(f"Ocorreu um erro ao buscar o usuário {nome_usuario}. Erro={erro}")
            raise erro
