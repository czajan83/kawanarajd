import uuid
from typing import Type, List

from sqlalchemy.orm import Session

from code.database.models import Sauces
from code.http.models import SaucesModel, SaucesResponseModel, Ingredient
from code.repository import raws as rep_raws


def get_sauces(db: Session) -> List[SaucesResponseModel]:
    sauces_db = db.query(Sauces).all()
    sauces_http = []
    for sauce_db in sauces_db:
        ingredients = extract_ingredients(sauce_db.recipe)
        sauces_http.append(SaucesResponseModel(id=sauce_db.id,
                                               name=sauce_db.name,
                                               ingredients=ingredients,
                                               final_amount_in_grams=sauce_db.final_amount_in_grams
        ))
    return sauces_http

def get_sauce(sauce_id: str, db: Session) -> SaucesResponseModel:
    sauce_db = search_sauce_by_id(sauce_id, db)
    ingredients = extract_ingredients(sauce_db.recipe)
    sauce_http = SaucesResponseModel(id=sauce_db.id,
                                    name=sauce_db.name,
                                    ingredients=ingredients,
                                    final_amount_in_grams=sauce_db.final_amount_in_grams
    )
    return sauce_http

def create_sauce(body: SaucesModel, db: Session) -> SaucesResponseModel:
    sauce = search_sauce_by_name(body.name, db)
    amount_sum = body.final_amount_in_grams
    if sauce is None:
        id_raw = uuid.uuid4().hex
        kcal_100g = fat = saturated_fat = carbohydrates = simple_sugars = fiber = proteins = salt = 0
        recipe = f""
        for ingredient in body.ingredients:
            raw = rep_raws.search_raw_by_id(ingredient.id, db)
            if raw is not None:
                amount = ingredient.amount_in_grams
                kcal_100g += raw.kcal_100g * amount
                fat += raw.fat * amount
                saturated_fat += raw.saturated_fat * amount
                carbohydrates += raw.carbohydrates * amount
                simple_sugars += raw.simple_sugars * amount
                fiber += raw.fiber * amount
                proteins += raw.proteins * amount
                salt += raw.salt * amount
                recipe += f"{ingredient.id}: {ingredient.amount_in_grams:.1f}, "

        sauce_db = Sauces(id=id_raw,
                          name=body.name,
                          kcal_100g=kcal_100g/amount_sum,
                          fat=fat/amount_sum,
                          saturated_fat=saturated_fat/amount_sum,
                          carbohydrates=carbohydrates/amount_sum,
                          simple_sugars=simple_sugars/amount_sum,
                          fiber=fiber/amount_sum,
                          proteins=proteins/amount_sum,
                          salt=salt/amount_sum,
                          recipe=recipe,
                          final_amount_in_grams=amount_sum

        )
        db.add(sauce_db)
        db.commit()
        db.refresh(sauce_db)

        sauce_http = SaucesResponseModel(id=id_raw,
                                         name=body.name,
                                         ingredients=body.ingredients,
                                         final_amount_in_grams=body.final_amount_in_grams
        )
    else:
        sauce_http = SaucesResponseModel(id=sauce.id,
                                         name=body.name,
                                         ingredients=body.ingredients,
                                         final_amount_in_grams=body.final_amount_in_grams
        )
    return sauce_http

def search_sauce_by_id(sauce_id: str, db: Session) -> Type[Sauces] | None:
    existing_sauces = db.query(Sauces).all()
    for sauce in existing_sauces:
        if sauce_id == sauce.id:
            return sauce
    return None

def search_sauce_by_name(sauce_name: str, db: Session) -> Type[Sauces] | None:
    existing_sauces = db.query(Sauces).all()
    for sauce in existing_sauces:
        if sauce_name == sauce.name:
            return sauce
    return None

def extract_ingredients(sauce_recipe: str) -> List[Ingredient]:
    ingredients_list = sauce_recipe.split(f", ")
    ingredients_list.pop(-1)
    out_ingredients = []
    for ingredient_str in ingredients_list:
        ingredient_parts = ingredient_str.split(f": ")
        ingredient = Ingredient(id=ingredient_parts[0], amount_in_grams=float(ingredient_parts[1]))
        out_ingredients.append(ingredient)
    return out_ingredients