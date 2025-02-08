import logging
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import boto3

from infraestructure.repositories.notificacao_interface import NotificacaoInterface

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class NotificacaoSms(NotificacaoInterface):

    def __init__(self, aws_region: str = "us-east-1"):
        self.ses_client = boto3.client('ses', region_name=aws_region)

    def enviar_notificacao(self, to_address: str, nome_usuario: str, message: str):
        from_address = os.getenv('EMAIL_USER')
        password = os.getenv('EMAIL_PASSWORD')

        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = "Atualizacao de status de processamento o seu video!"
        msg.attach(MIMEText(message, 'plain'))

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(from_address, password)

            server.sendmail(from_address, to_address, msg.as_string())
            print("Email enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar email: {str(e)}")
        finally:
            server.quit()
