from settings.config import MAILER_SERVER, MAILER_PORT, MAILER_HOST, MAILER_PASSWORD
from jinja2 import Environment, FileSystemLoader
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mailer:

    def __init__(
                    self, 
                    receiver_email: str,
                    subject: str, 
                    template_path: str, 
                    context: dict
                ) -> None:
        self._template_path = template_path
        self._subject = subject
        self._context = context
        self._receiver_email = receiver_email

    def send_notification(self):
        # Configuración para Jinja2
        env = Environment(loader=FileSystemLoader('app/templates'))

        # Cargar la plantilla HTML
        template = env.get_template(self._template_path)

        # Renderizar la plantilla con los datos específicos
        email_body = template.render(context=self._context)

        # Crear el mensaje MIME
        msg = MIMEMultipart()
        msg['From'] = MAILER_HOST
        msg['To'] = self._receiver_email
        msg['Subject'] = self._subject

        # Adjuntar el cuerpo del correo como HTML
        msg.attach(MIMEText(email_body, 'html'))

        # Iniciar una conexión SMTP y enviar el correo
        with smtplib.SMTP(MAILER_SERVER, MAILER_PORT) as server:
            server.starttls()
            server.login(MAILER_HOST, MAILER_PASSWORD)
            server.sendmail(MAILER_HOST, self._receiver_email, msg.as_string())
