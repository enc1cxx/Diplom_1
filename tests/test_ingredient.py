from ingredient import Ingredient
from ingredient_types import IngredientType
import pytest

from tests_data.tests_data_ingredient import DataIngredient


class TestIngredientGetName:

    def test_get_name(self):
        ingredient = Ingredient(IngredientType.FILLING, "Sausage", 2.99)
        assert ingredient.get_name() == "Sausage"

    # вряд ли ингредиент должен быть безымянным, 
    # но так как требований нет - проверим так
    def test_get_empty_name(self):
        ingredient = Ingredient(IngredientType.FILLING, "", 2.99)
        assert ingredient.get_name() != ""


class TestIngredientGetPrice:

    # проверим частный случай, а заодно, что float никуда не округлился
    def test_get_price(self):
        ingredient = Ingredient(IngredientType.FILLING, "Sausage", 2.99)
        assert ingredient.get_price() == 2.99

    # проверим, что с целыми тоже нормально работает
    def test_get_priceint(self):
        ingredient = Ingredient(IngredientType.FILLING, "Sausage", 3)
        assert ingredient.get_price() == 3

    # бесплатный ингредиент - вполне возможно
    def test_get_zero_price(self):
        ingredient = Ingredient(IngredientType.FILLING, "Sausage", 0)
        assert ingredient.get_price() == 0

    # вряд ли за проданный ингредиент продавец будет доплачивать, 
    # но так как требований нет - проверим так
    def test_get_negative_price(self):
        ingredient = Ingredient(IngredientType.FILLING, "Sausage", -5)
        assert ingredient.get_price() != -5


class TestIngredientGetType:

    @pytest.mark.parametrize(
        "ingredient_type, expected_type", DataIngredient.ingredients
    )
    def test_get_type(self, ingredient_type, expected_type):
        ingredient = Ingredient(ingredient_type, "Secret Ingredient", 1)
        assert ingredient.get_type() == expected_type