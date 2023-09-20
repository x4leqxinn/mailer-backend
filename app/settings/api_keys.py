from fastapi import Depends, HTTPException, status
from fastapi.security.api_key import APIKeyHeader

# Some key
api_keys = {
    '1': 'jorge',
}

def api_key_exist(api_key: str):
    """Verify client"""
    return api_keys.get(api_key)

def verify_api_key(api_key: str = Depends(APIKeyHeader(name='X-API-Key'))):
    """Verify access"""
    if not api_key_exist(api_key): 
        raise HTTPException(
                detail='Invalid credentials.',
                status_code=status.HTTP_401_UNAUTHORIZED, 
            )
    return api_key
