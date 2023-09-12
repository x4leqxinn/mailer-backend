from fastapi import APIRouter,status
from models.mailer_serializer import MailerCreateSerializer
from fastapi import Depends
from fastapi.security.api_key import APIKey
from settings.api_keys import verify_api_key

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
def send_email(content: MailerCreateSerializer,api_key: APIKey = Depends(verify_api_key)):
    return {'uwu': 1}
