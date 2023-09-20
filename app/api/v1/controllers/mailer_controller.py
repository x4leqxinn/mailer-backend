from fastapi import APIRouter,status
from models.serializers.mailer_serializer import MailerCreateSerializer
from fastapi import Depends
from fastapi.security.api_key import APIKey
from settings.api_keys import verify_api_key
from models.mailer import Mailer
import threading

router = APIRouter(
    prefix='/mailer',
    tags=['Mailer v1'],
    responses={ status.HTTP_404_NOT_FOUND: { 'mailer': 'Not found' } }
)
@router.post(
    '/', 
    response_model=None, 
    description='Send email'
)
async def send_email(content: MailerCreateSerializer,api_key: APIKey = Depends(verify_api_key)):
    
    email_sender = Mailer(
        receiver_email=content.receiver_email,
        subject = content.subject, 
        template_path = '/quotation/new_quotation.html', 
        context=content.data 
        )

    thread = threading.Thread(target=email_sender.send_notification)
    thread.start()
    

    return {'message': 'The email will be sent shortly.'}


