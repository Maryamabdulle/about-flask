class Customer:
    """Ubermelon customer."""

    cart = {}

    def __init__(self, first, last, email, password):
        self.first = first
        self.last = last
        self.name = first + ' ' + last
        self.email = email
        self.password = password