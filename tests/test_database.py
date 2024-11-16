from database import Database


class TestAvailableBuns:

    def test_get_available_buns(self):
        database = Database()
        list_of_buns = database.available_buns()
        assert len(list_of_buns) == 3 and \
            list_of_buns[0].get_name() == "black bun" and \
            list_of_buns[1].get_name() == "white bun" and \
            list_of_buns[2].get_name() == "red bun"


class TestAvailableIngredients:
    def test_get_available_buns(self):
        database = Database()
        list_of_ingredients = database.available_ingredients()
        assert len(list_of_ingredients) == 6 and \
            list_of_ingredients[0].get_name() == "hot sauce" and \
            list_of_ingredients[1].get_name() == "sour cream" and \
            list_of_ingredients[2].get_name() == "chili sauce" and \
            list_of_ingredients[3].get_name() == "cutlet" and \
            list_of_ingredients[4].get_name() == "dinosaur" and \
            list_of_ingredients[5].get_name() == "sausage"
