import json
import redis
from app.config import REDIS_HOST, REDIS_PORT


#init redis client

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

def get_cache(key:str):
    try:
        return redis_client.get(key)
    except redis.RedisError:
        print("CACHE MISS !")
        return None


def set_cache(key:str,value:dict,ttl:int):
    try:
        redis_client.set(key,json.dumps(value),ex=ttl)
    except redis.RedisError :
        print("could not set a key")
        pass
    


def delete_cache(key: str):
    try:
        redis_client.delete(key)
    except redis.RedisError:
        pass