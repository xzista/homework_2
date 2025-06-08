class ZeroQuantityError(Exception):
    """Класс исключения, который отвечает за обработку добавления товара с нулевым количеством."""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Попытка добавления товара с нулевым количеством"

    def __str__(self):
        return self.message
