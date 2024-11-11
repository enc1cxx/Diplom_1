import pytest
from burger import Burger
from bun import Bun
from ingredient import Ingredient
from ingredient_types import IngredientType
from tests_data.tests_data_burger import DataBurgerIngredients


class TestCreateBurger:

    def test_create_empty_burger(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []


class TestSetBuns:

    def test_set_buns(self):
        burger = Burger()
        bun = Bun("Soft bun", 3.99)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_double_set_buns(self):
        burger = Burger()
        bun_1 = Bun("Soft bun", 3.99)
        bun_2 = Bun("Crispy bun", 3.99)
        burger.set_buns(bun_1)
        burger.set_buns(bun_2)
        assert burger.bun == bun_2


class TestAddIngredient:

    @pytest.mark.parametrize("ingredient_type", DataBurgerIngredients.ingredients)
    def test_add_ingredient(self, ingredient_type: str):
        burger = Burger()
        ingredient = Ingredient(ingredient_type, "Secret Ingredient", 1)
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]


class TestMoveIngredient:

    def test_move_ingredient_backward(self):
        burger = Burger()
        ingredient_1 = Ingredient(IngredientType.SAUCE, "Soy sauce", 0.5)
        ingredient_2 = Ingredient(IngredientType.FILLING, "Cutlet", 1.5)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == ingredient_2

    def test_move_ingredient_forward(self):
        burger = Burger()
        ingredient_1 = Ingredient(IngredientType.SAUCE, "Soy sauce", 0.5)
        ingredient_2 = Ingredient(IngredientType.FILLING, "Cutlet", 1.5)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient_2

    def test_move_ingredient_same_index(self):
        burger = Burger()
        ingredient_1 = Ingredient(IngredientType.SAUCE, "Soy sauce", 0.5)
        ingredient_2 = Ingredient(IngredientType.FILLING, "Cutlet", 1.5)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 0)
        assert burger.ingredients[0] == ingredient_1

    # Так как никаких требований нет, то будем считать,
    # что метод должен быть как минимум безопасным к таким операциям
    def test_move_ingredient_empty_ingredients(self):
        try:
            burger = Burger()
            burger.move_ingredient(0, 1)
        except IndexError:
            assert False


class TestRemoveIngredient:

    def test_remove_single_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(IngredientType.SAUCE, "Soy sauce", 0.5)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_remove_first_ingredient(self):
        burger = Burger()
        ingredient_1 = Ingredient(IngredientType.SAUCE, "Cutlet 1", 0.5)
        ingredient_2 = Ingredient(IngredientType.SAUCE, "Cutlet 2", 0.5)
        ingredient_3 = Ingredient(IngredientType.SAUCE, "Cutlet 3", 0.5)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.add_ingredient(ingredient_3)
        burger.remove_ingredient(0)
        assert burger.ingredients == [ingredient_2, ingredient_3]

    def test_remove_last_ingredient(self):
        burger = Burger()
        ingredient_1 = Ingredient(IngredientType.SAUCE, "Cutlet 1", 0.5)
        ingredient_2 = Ingredient(IngredientType.SAUCE, "Cutlet 2", 0.5)
        ingredient_3 = Ingredient(IngredientType.SAUCE, "Cutlet 3", 0.5)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.add_ingredient(ingredient_3)
        burger.remove_ingredient(2)
        assert burger.ingredients == [ingredient_1, ingredient_2]

    # Так как никаких требований нет, то будем считать,
    # что метод должен быть как минимум безопасным к таким операциям
    def test_remove_ingredient_from_empty_ingredients_list(self):
        burger = Burger()
        try:
            burger.remove_ingredient(0)
        except IndexError:
            assert False

    # Так как никаких требований нет, то будем считать,
    # что метод должен быть как минимум безопасным к таким операциям
    def test_remove_ingredient_with_incorrect_index(self):
        burger = Burger()
        ingredient_1 = Ingredient(IngredientType.SAUCE, "Cutlet 1", 0.5)
        burger.add_ingredient(ingredient_1)
        try:
            burger.remove_ingredient(1)
        except IndexError:
            assert False


class TestGetPrice:

    def test_correct_burger_get_price(self):
        burger = Burger()
        bun = Bun("Soft bun", 2.50)
        ingredient_1 = Ingredient(IngredientType.SAUCE, "Soy sauce", 0.5)
        ingredient_2 = Ingredient(IngredientType.FILLING, "Cutlet", 1.5)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        assert burger.get_price() == 7.0

    # Так как никаких требований нет, то будем считать,
    # что запрос к некомплектному бургеру должен вернуть стоимость того,
    # что в бургере есть, иначе = 0
    def test_burger_without_buns_get_price(self):
        burger = Burger()
        ingredient_1 = Ingredient(IngredientType.SAUCE, "Soy sauce", 0.5)
        ingredient_2 = Ingredient(IngredientType.FILLING, "Cutlet", 1.5)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        assert burger.get_price() == 2.0

    def test_burger_without_ingredients_get_price(self):
        burger = Burger()
        bun = Bun("Soft bun", 2.50)
        burger.set_buns(bun)
        assert burger.get_price() == 5.0

    # Так как никаких требований нет, то будем считать,
    # что запрос к некомплектному бургеру должен вернуть стоимость того,
    # что в бургере есть, иначе = 0
    def test_empty_burger_get_price(self):
        burger = Burger()
        assert burger.get_price() == 0.0


class TestGetReciept:

    def test_correct_burger_get_receipt(self):
        burger = Burger()
        bun = Bun("Soft bun", 2.50)
        ingredient_1 = Ingredient(IngredientType.SAUCE, "Soy sauce", 0.5)
        ingredient_2 = Ingredient(IngredientType.FILLING, "Cutlet", 1.5)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        expected_receipt = "(==== Soft bun ====)\n= sauce Soy sauce =\n= filling Cutlet =\n(==== Soft bun ====)\n\nPrice: 7.0"
        assert burger.get_receipt() == expected_receipt

    def test_burger_without_ingredients_get_receipt(self):
        burger = Burger()
        bun = Bun("Soft bun", 2.50)
        burger.set_buns(bun)
        expected_receipt = "(==== Soft bun ====)\n(==== Soft bun ====)\n\nPrice: 5.0"
        assert burger.get_receipt() == expected_receipt

    # Так как никаких требований нет, то будем считать,
    # что запрос к неполному бургеру должен вернуть чек с теми ингредиентами,
    # что есть в бургере и их стоимостью
    def test_burger_without_buns_get_receipt(self):
        burger = Burger()
        ingredient_1 = Ingredient(IngredientType.SAUCE, "Soy sauce", 0.5)
        ingredient_2 = Ingredient(IngredientType.FILLING, "Cutlet", 1.5)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        expected_receipt = "\n= sauce Soy sauce =\n= filling Cutlet =\n\n\nPrice: 2.0"
        assert burger.get_receipt() == expected_receipt

    # Так как никаких требований нет, то будем считать,
    # что запрос к неполному бургеру должен вернуть чек с теми ингредиентами,
    # что есть в бургере и их стоимостью
    def test_empty_burger_get_receipt(self):
        burger = Burger()
        expected_receipt = "\n\nPrice: 0.0"
        assert burger.get_receipt() == expected_receipt
