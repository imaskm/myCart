
class Product:

    def __init__(self, _id, name, price, categories=tuple()):
        self.__id = _id
        self.name = name
        self.price = price
        self.categories = categories

    def get_id(self):
        return self.__id

    def __iter__(self):

        yield self.get_id()
        yield self.name
        yield self.price
        yield self.categories

    @staticmethod
    def headers():
        return [ 'Product ID', 'Name', 'Price', 'Categories' ]


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self ,name):
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, categories):
        self._categories = categories
