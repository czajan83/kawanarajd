from typing import List

from sqlalchemy import and_
from sqlalchemy.orm import Session

from code.database.models import Recipes, Dishes
from code.http.models import RecipesModel
from code.repository import dishes as rep_dishes



class RepRecipes:
    kcal_100g = 0
    fat = 0
    saturated_fat = 0
    carbohydrates = 0
    simple_sugars = 0
    fiber = 0
    proteins = 0
    salt = 0

    @staticmethod
    def get_recipes(db: Session) -> List[RecipesModel]:
        recipes = []
        recipes_ids = []
        components_ids = []
        amounts = []

        recipes_db = db.query(Recipes).all()
        for recipe_db in recipes_db:
            recipes_ids.append(recipe_db.recipe_id)
        recipes_ids_set = set(recipes_ids)
        for recipe_id in recipes_ids_set:
            dish_name = db.query(Dishes).filter(and_(Dishes.id == recipe_id)).first().name
            for recipe_db in recipes_db:
                if recipe_db.recipe_id == recipe_id:
                    components_ids.append(recipe_db.component_id)
                    amounts.append(recipe_db.amount)
            recipes.append(RecipesModel(name=dish_name, recipe_ids=components_ids, recipe_amounts=amounts))
            components_ids.clear()
            amounts.clear()

        return recipes

    @staticmethod
    def get_recipe(recipe_id: int, db: Session) -> RecipesModel | None:

        components_ids = []
        amounts = []

        recipes_db = db.query(Recipes).all()
        dish_name = db.query(Dishes).filter(and_(Dishes.id == recipe_id)).first()
        if dish_name is None:
            return None
        for recipe_db in recipes_db:
            if recipe_db.recipe_id == recipe_id:
                components_ids.append(recipe_db.component_id)
                amounts.append(recipe_db.amount)
        recipe = RecipesModel(name=dish_name.name, recipe_ids=components_ids, recipe_amounts=amounts)
        components_ids.clear()
        amounts.clear()

        return recipe
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

    def create_recipe(self, body: RecipesModel, db: Session) -> RecipesModel | int:

        if RepRecipes.validate_body(body=body) < 0:
            return -1
        dish = rep_dishes.search_dish_by_name(body.name, db)

        if dish is None:
            if self.calculate_nutritional_values(body=body, db=db) < 0:
                return -2
            dish_db = Dishes(name=body.name,
                             kcal_100g=self.kcal_100g,
                             fat=self.fat,
                             saturated_fat=self.saturated_fat,
                             carbohydrates=self.carbohydrates,
                             simple_sugars=self.simple_sugars,
                             fiber=self.fiber,
                             proteins=self.proteins,
                             salt=self.salt)
            db.add(dish_db)
            db.commit()
            db.refresh(dish_db)
            dish_db_added = rep_dishes.search_dish_by_name(body.name, db)

            for index, component_id in enumerate(body.recipe_ids):
                recipe_db = Recipes(recipe_id=dish_db_added.id,
                                    component_id=body.recipe_ids[index],
                                    amount=body.recipe_amounts[index])
                db.add(recipe_db)
            db.commit()
        return body

    def update_recipe(self, recipe_id: int, body: RecipesModel, db: Session) -> RecipesModel | int:

        if RepRecipes.validate_body(body=body) < 0:
            return -1
        dish = rep_dishes.search_dish_by_id(recipe_id, db)
        recipes = db.query(Recipes).filter(and_(Recipes.recipe_id == dish.id)).all()

        if dish is not None:
            if dish.name != body.name:
                return -2
            if self.calculate_nutritional_values(body=body, db=db) < 0:
                return -4
            dish.kcal_100g = self.kcal_100g
            dish.fat = self.fat
            dish.saturated_fat = self.saturated_fat
            dish.carbohydrates = self.carbohydrates
            dish.simple_sugars = self.simple_sugars
            dish.fiber = self.fiber
            dish.proteins = self.proteins
            dish.salt = self.salt
            db.commit()
            for recipe_db in recipes:
                db.delete(recipe_db)
            db.commit()
            for index, component_id in enumerate(body.recipe_ids):
                recipe_db = Recipes(recipe_id=recipe_id,
                                    component_id=body.recipe_ids[index],
                                    amount=body.recipe_amounts[index])
                db.add(recipe_db)
            db.commit()
        return body

    @staticmethod
    def remove_recipe(recipe_id: int, body: RecipesModel, db: Session) -> int:

        dish = rep_dishes.search_dish_by_id(recipe_id, db)

        if dish is not None:
            if dish.name != body.name:
                return -1
            db.delete(dish)
            db.commit()
        return 0

    def calculate_nutritional_values(self, body: RecipesModel, db: Session) -> int:

        dish_amount = sum(body.recipe_amounts)

        for index, component_id in enumerate(body.recipe_ids):
            component = rep_dishes.search_dish_by_id(component_id, db)
            if component is None:
                return -1
            self.kcal_100g += component.kcal_100g * body.recipe_amounts[index]
            self.fat += component.fat * body.recipe_amounts[index]
            self.saturated_fat += component.saturated_fat * body.recipe_amounts[index]
            self.carbohydrates += component.carbohydrates * body.recipe_amounts[index]
            self.simple_sugars += component.simple_sugars * body.recipe_amounts[index]
            self.fiber += component.fiber * body.recipe_amounts[index]
            self.proteins += component.proteins * body.recipe_amounts[index]
            self.salt += component.salt * body.recipe_amounts[index]

        self.kcal_100g /= dish_amount
        self.fat /= dish_amount
        self.saturated_fat /= dish_amount
        self.carbohydrates /= dish_amount
        self.simple_sugars /= dish_amount
        self.fiber /= dish_amount
        self.proteins /= dish_amount
        self.salt /= dish_amount

        return 0

    @staticmethod
    def validate_body(body: RecipesModel) -> int:
        if len(body.recipe_ids) != len(body.recipe_amounts):
            return -1
        if len(body.recipe_ids) != len(set(body.recipe_ids)):
            return -2
        return 0

    @staticmethod
    def search_recipes_by_dish_id(dish_id: int, db: Session):
        return

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