from fastapi import APIRouter
from starlette import status

router = APIRouter()

@router.get("/hello")
def root():
    return {"message": "Hello World!!!"}