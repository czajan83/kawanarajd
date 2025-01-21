from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from code.database.database import get_db
from code.http.models import RecipesResponseModel, RecipesModel
from code.repository import recipes as rep_recipes

router = APIRouter(prefix="/recipes", tags=["recipes"])

# @router.get("/", response_model=List[SaucesResponseModel])
# def get_sauces(db: Session = Depends(get_db)):
#     sauces = rep_sauces.get_sauces(db)
#     if not sauces:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="sauces not found")
#     return sauces
#
# @router.get("/{sauce_id}", response_model=SaucesResponseModel)
# def get_raw(sauce_id: str, db: Session = Depends(get_db)):
#     sauce = rep_sauces.get_sauce(sauce_id, db)
#     if sauce is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="sauce not found")
#     return sauce

@router.post("/", response_model=RecipesResponseModel, status_code=status.HTTP_201_CREATED)
def create_recipe(body: RecipesModel, db: Session = Depends(get_db)):
    recipes = rep_recipes.create_recipe(body, db)
    if recipes == -1:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="function not implementes")
    return recipes

# @router.put("/{sauce_id}", response_model=SaucesResponseModel)
# def put_sauce(sauce_id: str, body: SaucesModel, db: Session = Depends(get_db)):
#     sauce = rep_sauces.update_sauce(sauce_id, body, db)
#     if sauce == -1:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="sauce not found")
#     if sauce == -2:
#         raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="sauce name incorrect")
#     return sauce
#
# @router.delete("/{sauce_id}", response_model=List[SaucesResponseModel])
# def delete_raw(sauce_id: str, body: SaucesModel, db: Session = Depends(get_db)):
#     sauce = rep_sauces.remove_sauce(sauce_id, body, db)
#     if sauce == -1:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="sauce not found")
#     if sauce == -2:
#         raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="sauce name incorrect")
#     return []