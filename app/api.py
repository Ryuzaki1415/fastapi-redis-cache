import json
import time
from fastapi import APIRouter

from app.cache import get_cache,set_cache,delete_cache
from app.mock_api import fetch_user_from_slow_source
from app.config import CACHE_TTL


router=APIRouter()


@router.get("/users/{user_id}")
def get_user(user_id:int):
    start=time.time()
    cache_key=user_id
    
    cached_check=get_cache(user_id)
    
    if cached_check:
        
        print("CACHE HIT !")
        return{
            "data": json.loads(cached_check),
            "cached": True,
            "response_time_ms": int((time.time() - start) * 1000)
        }
    print("CACHE MISS !")
    data = fetch_user_from_slow_source(user_id)
    set_cache(cache_key, data, CACHE_TTL)
    return {
        "data": data,
        "cached": False,
        "response_time_ms": int((time.time() - start) * 1000)
    }
    
@router.delete("/users/{user_id}/cache")
def invalidate_cache(user_id: int):
    cache_key = f"user:{user_id}"
    delete_cache(cache_key)
    return {"message": "Cache invalidated"}