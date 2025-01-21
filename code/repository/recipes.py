import uuid
from typing import Type, List

from sqlalchemy.orm import Session

from code.database.models import Recipes
from code.http.models import RecipesModel, RecipesResponseModel, Ingredient
from code.repository import dishes as rep_dishes


# def get_sauces(db: Session) -> List[SaucesResponseModel]:
#     sauces_db = db.query(Sauces).all()
#     sauces_http = []
#     for sauce_db in sauces_db:
#         ingredients = extract_ingredients(sauce_db.recipe)
#         sauces_http.append(SaucesResponseModel(id=sauce_db.id,
#                                                name=sauce_db.name,
#                                                ingredients=ingredients,
#                                                final_amount_in_grams=sauce_db.final_amount_in_grams
#         ))
#     return sauces_http
#
# def get_sauce(sauce_id: str, db: Session) -> SaucesResponseModel:
#     sauce_db = search_sauce_by_id(sauce_id, db)
#     ingredients = extract_ingredients(sauce_db.recipe)
#     sauce_http = SaucesResponseModel(id=sauce_db.id,
#                                     name=sauce_db.name,
#                                     ingredients=ingredients,
#                                     final_amount_in_grams=sauce_db.final_amount_in_grams
#     )
#     return sauce_http

def create_recipe(body: RecipesModel, db: Session) -> RecipesResponseModel | int:
    dish = rep_dishes.search_dish_by_name(body.name, db)
    # amount_sum = body.final_amount_in_grams
    if dish is None:
        dishes = rep_dishes.get_dishes(db)
        for index, component_id in enumerate(body.recipe_ids):
            component = rep_dishes.search_dish_by_id(component_id, db)
            print(component.id)
            print(body.recipe_amounts[index])


    #     id_sauce = uuid.uuid4().hex
    #     kcal_100g = fat = saturated_fat = carbohydrates = simple_sugars = fiber = proteins = salt = 0
    #     recipe = f""
    #
    #     sauce_db = Sauces(id=id_sauce,
    #                       name=body.name,
    #                       kcal_100g=kcal_100g/amount_sum,
    #                       fat=fat/amount_sum,
    #                       saturated_fat=saturated_fat/amount_sum,
    #                       carbohydrates=carbohydrates/amount_sum,
    #                       simple_sugars=simple_sugars/amount_sum,
    #                       fiber=fiber/amount_sum,
    #                       proteins=proteins/amount_sum,
    #                       salt=salt/amount_sum,
    #                       recipe=recipe,
    #                       final_amount_in_grams=amount_sum
    #
    #     )
    #     db.add(sauce_db)
    #     db.commit()
    #     db.refresh(sauce_db)
    #
    #     sauce_http = SaucesResponseModel(id=id_sauce,
    #                                      name=body.name,
    #                                      ingredients=body.ingredients,
    #                                      final_amount_in_grams=body.final_amount_in_grams
    #     )
    # else:
    #     sauce_http = SaucesResponseModel(id=sauce.id,
    #                                      name=body.name,
    #                                      ingredients=body.ingredients,
    #                                      final_amount_in_grams=body.final_amount_in_grams
    #     )
    return -1

# def update_sauce(sauce_id: str, body: SaucesModel, db: Session) -> SaucesResponseModel | int:
#     sauce = search_sauce_by_id(sauce_id, db)
#     amount_sum = body.final_amount_in_grams
#     if sauce is not None:
#         if sauce.name != body.name:
#             return -2
#         kcal_100g = fat = saturated_fat = carbohydrates = simple_sugars = fiber = proteins = salt = 0
#         sauce.kcal_100g=kcal_100g/amount_sum
#         sauce.fat=fat/amount_sum
#         sauce.saturated_fat=saturated_fat/amount_sum
#         sauce.carbohydrates=carbohydrates/amount_sum
#         sauce.simple_sugars=simple_sugars/amount_sum
#         sauce.fiber=fiber/amount_sum
#         sauce.proteins=proteins/amount_sum
#         sauce.salt=salt/amount_sum
#         db.commit()
#         sauce_http = SaucesResponseModel(id=sauce.id,
#                                          name=body.name,
#                                          ingredients=body.ingredients,
#                                          final_amount_in_grams=body.final_amount_in_grams
#         )
#         return sauce_http
#     return -1
#
# def remove_sauce(sauce_id: str, body: SaucesModel, db: Session) -> int | None:
#     existing_sauce = search_sauce_by_id(sauce_id, db)
#     if existing_sauce is not None:
#         if existing_sauce.name != body.name:
#             return -2
#         db.delete(existing_sauce)
#         db.commit()
#         return 0
#     return -1
#
# def search_sauce_by_id(sauce_id: str, db: Session) -> Type[Sauces] | None:
#     existing_sauces = db.query(Sauces).all()
#     for sauce in existing_sauces:
#         if sauce_id == sauce.id:
#             return sauce
#     return None
#
# def search_sauce_by_name(sauce_name: str, db: Session) -> Type[Sauces] | None:
#     existing_sauces = db.query(Sauces).all()
#     for sauce in existing_sauces:
#         if sauce_name == sauce.name:
#             return sauce
#     return None
#
# def extract_ingredients(sauce_recipe: str) -> List[Ingredient]:
#     ingredients_list = sauce_recipe.split(f", ")
#     ingredients_list.pop(-1)
#     out_ingredients = []
#     for ingredient_str in ingredients_list:
#         ingredient_parts = ingredient_str.split(f": ")
#         ingredient = Ingredient(id=ingredient_parts[0], amount_in_grams=float(ingredient_parts[1]))
#         out_ingredients.append(ingredient)
#     return out_ingredients