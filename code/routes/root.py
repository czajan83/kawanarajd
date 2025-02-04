from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def root():
    return {"message": "Hello World!!!"}