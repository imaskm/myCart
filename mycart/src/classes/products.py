
class Product:

    def __init__(self, _id, name, price, quantity ,categories=tuple()):
        self.__id = _id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.categories = categories

    def get_id(self):
        return self.__id

    def __iter__(self):

        yield self.get_id()
        yield self.name
        yield self.price
        yield self.quantity
        yield self.categories

    @staticmethod
    def headers():
        return ['Product ID', 'Name', 'Price', 'Availability', 'Categories' ]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def quantity(self):
        return self._quantity

        # if self._quantity and self._quantity > 0:
        #     return "In Stock"
        # else:
        #     return "Out of Stock"

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = int(quantity) if quantity else 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def categories(self):
        if self._categories:
            return ','.join(self._categories)
        else:
            return ""

    @categories.setter
    def categories(self, categories):
        self._categories = categories
