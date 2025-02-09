import json
import logging

from application.service.buscar_telefone_usuario_usecase import BuscarTelefoneUsuarioUseCase
from application.usecases.notificacao_email import NotificacaoEmail
from application.usecases.notificacao_sms import NotificacaoSms
from domain.interfaces.notificacao import Notificacao
from infraestructure.repositories.cognito_repository_impl import CognitoRepositoryImpl

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

cognito_repository = CognitoRepositoryImpl()
buscar_telefone_usuario_usecase = BuscarTelefoneUsuarioUseCase(cognito_repository)

senders = {
    "EMAIL": NotificacaoEmail(),
    "SMS": NotificacaoSms(buscar_telefone_usuario_usecase)
}


def lambda_handler(event, context):
    logger.info(f"Mensagem recebida={event}")

    body = json.loads(event['Records'][0]['body'])
    nome_usuario = body.get('nome_usuario')
    tipo_comunicacao = body.get('tipo_comunicacao', "EMAIL")
    mensagem = body.get('mensagem')

    if not nome_usuario or not mensagem:
        logger.error("Payload inválido. Campos necessários: nome_usuario, mensagem.")
        return

    sender: Notificacao = senders.get(tipo_comunicacao)
    sender.notificar(nome_usuario, mensagem)

    logger.info(f"Notificação enviada com sucesso")
    return {"statusCode": 200, "body": "Processamento concluído"}


if __name__ == '__main__':
    event = {
        "Records": [
            {
                "body": '{"nome_usuario":"gustavozenke", "mensagem": "mensagem teste", "tipo_comunicacao": "Email"}',
            }
        ]
    }
    lambda_handler(event, None)
