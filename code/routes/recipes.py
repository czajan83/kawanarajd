from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from code.database.database import get_db
from code.http.models import RecipesModel
from code.repository.recipes import RepRecipes

router = APIRouter(prefix="/recipes", tags=["recipes"])

@router.get("/", response_model=List[RecipesModel])
def get_recipes(db: Session = Depends(get_db)):
    recipe_obj = RepRecipes()
    recipes = recipe_obj.get_recipes(db)
    if not recipes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="recipes not found")
    return recipes

@router.get("/{recipe_id}", response_model=RecipesModel)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe_obj = RepRecipes()
    recipe = recipe_obj.get_recipe(recipe_id, db)
    if recipe is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="recipe not found")
    return recipe

@router.post("/", response_model=RecipesModel, status_code=status.HTTP_201_CREATED)
def create_recipe(body: RecipesModel, db: Session = Depends(get_db)):
    recipe_obj = RepRecipes()
    recipes = recipe_obj.create_recipe(body, db)
    if recipes == -1:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="lengths od recipe_ids and recipe_amounts not equal "
                                   "or elements in recipe_ids list are not unique")
    if recipes == -2:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="one or more components in recipe_ids list not found in database, "
                                   "please check the recipe_ids")
    return recipes

@router.put("/{recipe_id}", response_model=RecipesModel)
def put_recipe(recipe_id: int, body: RecipesModel, db: Session = Depends(get_db)):
    recipe_obj = RepRecipes()
    recipes = recipe_obj.update_recipe(recipe_id, body, db)
    if recipes == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="recipe not found")
    if recipes == -2:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="recipe name incorrect")
    if recipes == -3:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="one or more components in recipe_ids list not found in database, "
                                   "please check the recipe_ids")
    return recipes

@router.delete("/{recipe_id}")
def put_recipe(recipe_id: int, body: RecipesModel, db: Session = Depends(get_db)):
    recipe_obj = RepRecipes()
    recipes = recipe_obj.remove_recipe(recipe_id, body, db)
    if recipes == -2:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="recipe not found")
    if recipes == -1:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="recipe name incorrect")
    return []
