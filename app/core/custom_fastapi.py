from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from settings.config import *
import os
import time


class CustomFastAPI(FastAPI):

    def __init__(self):
        kwargs = \
        {
            'title' : 'Mailer backend [latest]',
            'description' : 'a REST API',
            'version' : CURRENT_VERSION,
            'openapi_tags' : TAGS_METADATA,
            'openapi_url' : '/openapi',
            'docs_url' : '/docs',
            'redoc_url' : '/redocs',
        }     
        super().__init__(**kwargs)
        self.configure()
    
    """GETTERS"""
    @property
    def server_timezone(self): return self.__server_timezone

    def configure(self):
        # Config app
        self.setup_server_timezone()
        self.setup_middlewares()
        self.setup_base_routes()
        self.setup_routes()
        self.setup_events()

    def setup_server_timezone(self):
        tz = TIMEZONE
        os.environ['TZ'] = tz
        time.tzset()
        self.__server_timezone = tz

    def setup_middlewares(self):
        self.add_middleware(
            CORSMiddleware,
            allow_origins=ALLOW_ORIGINS,
            allow_credentials=ALLOW_CREDENTIALS,
            allow_methods=ALLOW_METHODS,
            allow_headers=ALLOW_HEADERS,
            expose_headers=EXPOSE_HEADERS
        ) 

    def setup_base_routes(self):
        
        """MAIN PATH"""
        @self.get("/", include_in_schema=False)
        async def root(): return {'response': 'Ping!'}

    def setup_routes(self):
        """API ROUTER"""
        from api.v1.controllers import mailer_router
        
        # V1 ROUTER
        v1_router = APIRouter()
        
        # Controllers
        v1_router.include_router(mailer_router,prefix=VERSION.get(1))
        
        # API ROUTER
        api_router = APIRouter()
        api_router.include_router(v1_router,prefix='/api')
        
        # GLOBAL ROUTER
        self.include_router(api_router)



    def setup_events(self):
        """GLOBAL EVENTS"""
        @self.on_event("startup")
        async def startup_event(): pass

        @self.on_event("shutdown")
        async def shutdown(): pass

