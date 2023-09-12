from pydantic import BaseModel, constr, conint, EmailStr, validator
from typing import Optional

class MailerCreateSerializer(BaseModel):
    receiver_email: EmailStr
    subject: constr(min_length=3, max_length=15)
    kind: conint(ge=1, le=2)
    name: Optional[str] = None  # Asegúrate de que los campos opcionales tengan un valor predeterminado
    body: Optional[str] = None
    data: Optional[str]

    @validator("receiver_email")
    def validate_receiver_email(cls, value):
        # Validar la dirección de correo electrónico utilizando una expresión regular
        import re
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value):
            raise ValueError("Formato de correo electrónico no válido")
        return value

    @validator("name", pre=True, always=True)
    def validate_name(cls, value, values):
        if values.get("kind") == 2 and value is None:
            raise ValueError("El campo 'name' es obligatorio cuando 'kind' es igual a 2")
        return value

    @validator("body", pre=True, always=True)
    def validate_body(cls, value, values):
        if values.get("kind") == 1 and value is None:
            raise ValueError("El campo 'body' es obligatorio cuando 'kind' es igual a 1")
        return value
