from typing import List

from bun import Bun
from ingredient import Ingredient
from ingredient_types import IngredientType


class Database:
    """
    Класс с методами по работе с базой данных.
    """

    def __init__(self):
        self.buns: List[Bun] = []
        self.ingredients: List[Ingredient] = []

        self.buns.append(Bun("black bun", 100))
        self.buns.append(Bun("white bun", 200))
        self.buns.append(Bun("red bun", 300))

        self.ingredients.append(Ingredient(IngredientType.SAUCE, "hot sauce", 100))
        self.ingredients.append(Ingredient(IngredientType.SAUCE, "sour cream", 200))
        self.ingredients.append(Ingredient(IngredientType.SAUCE, "chili sauce", 300))

        self.ingredients.append(Ingredient(IngredientType.FILLING, "cutlet", 100))
        self.ingredients.append(Ingredient(IngredientType.FILLING, "dinosaur", 200))
        self.ingredients.append(Ingredient(IngredientType.FILLING, "sausage", 300))

    def available_buns(self) -> List[Bun]:
        return self.buns

    def available_ingredients(self) -> List[Ingredient]:
        return self.ingredients
