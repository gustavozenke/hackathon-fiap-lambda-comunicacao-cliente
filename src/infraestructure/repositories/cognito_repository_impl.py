import os

import boto3
from botocore.exceptions import ClientError

from domain.interfaces.cognito_repository import CognitoRepository


class CognitoRepositoryImpl(CognitoRepository):

    def __init__(self):
        self.client_cognito = boto3.client('cognito-idp')

    def admin_get_user(self, nome_usuario):
        try:
            response = self.client_cognito.admin_get_user(
                UserPoolId=os.getenv("USER_POOL_ID"),
                Username=nome_usuario
            )
            return response
        except ClientError as e:
            print(f"Erro ao buscar o usuário: {e}")
            return None
