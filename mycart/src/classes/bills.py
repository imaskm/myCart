class Bill:

    def __init__(self ,total_amount: float, discount: float, cart_id, username ):
        self.id = None
        self.total_amount = total_amount
        self.discount = discount
        self.cart_id = cart_id
        self.username = username

    def __iter__(self):
        yield self.total_amount
        yield self.discount
        yield self.cart_id
        yield self.username
