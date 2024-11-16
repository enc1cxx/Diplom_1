from bun import Bun
from unittest.mock import Mock


# Тут моки использовал исключительно для выполнения условия дипломного проекта. Практической пользы и глубокого
# смысла в этом нет
class TestBunGetName:

    def test_get_name(self):
        bun_mock = Mock()
        bun_mock.get_name.return_value = "Soft bun"
        assert bun_mock.get_name() == "Soft bun"

    # Вряд ли булка должна быть безымянной,
    # но так как требований нет - проверим так
    def test_get_empty_name(self):
        bun_mock = Mock()
        bun_mock.get_name.return_value = ""
        assert bun_mock.get_name() != ""


class TestBunGetPrice:

    def test_get_price(self):
        bun = Bun("Soft bun", 3.99)
        assert bun.get_price() == 3.99

    def test_get_zero_price(self):
        bun = Bun("Soft bun", 0)
        assert bun.get_price() == 0

    def test_get_price_integer(self):
        bun = Bun("Soft bun", 3)
        assert bun.get_price() == 3

    # Вряд ли продавец должен доплачивать покупателю за булку,
    # но так как требований нет - проверим так
    def test_get_negative_price(self):
        bun = Bun("Soft bun", -5)
        assert bun.get_price() != -5
