from fastapi import FastAPI
from app.api import router


app=FastAPI(title="FastAPI cache with redis")

app.include_router(router)



