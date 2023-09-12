import uvicorn
from .custom_fastapi import CustomFastAPI
from settings.config import APP_HOST, APP_PORT

app = CustomFastAPI()

def start():
    uvicorn.run('core:app',host=APP_HOST,port=APP_PORT,reload=True)