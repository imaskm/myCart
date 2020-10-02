
class CartDetails:
    def __init__(self, _id, cart_id, product_id, quantity):
        self.__id = _id
        self.cart_id = cart_id
        self.product_id = product_id
        self.quantity = quantity

    @property
    def cart_id(self):
        return self._cart_id

    @cart_id.setter
    def cart_id(self, value):
        self._cart_id = value

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value




