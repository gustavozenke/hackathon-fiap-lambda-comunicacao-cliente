import os

import boto3

from domain.interfaces.cognito_repository import CognitoRepository


class CognitoRepositoryImpl(CognitoRepository):

    def __init__(self):
        self.client_cognito = boto3.client('cognito-idp')

    def admin_get_user(self, nome_usuario):
        return self.client_cognito.admin_get_user(
            UserPoolId=os.getenv("USER_POOL_ID"),
            Username=nome_usuario
        )
