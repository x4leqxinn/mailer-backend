from pydantic import BaseModel, constr, conint, EmailStr, validator
from typing import Optional

class MailerCreateSerializer(BaseModel):
    receiver_email: EmailStr
    subject: constr(min_length=3, max_length=80)
    data: dict # quotation, email, name, phone

    @validator("receiver_email")
    def validate_receiver_email(cls, value):
        # Validar la dirección de correo electrónico utilizando una expresión regular
        import re
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value):
            raise ValueError("Formato de correo electrónico no válido")
        return value
