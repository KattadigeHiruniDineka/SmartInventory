
class Product:
    def __init__(self, product_id, name, price, quantity, category):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.__price = 0
        self.__quantity = 0

        self.price = price
        self.quantity = quantity

    # Encapsulation: control price changes
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be greater than zero.")
        self.__price = value

    # Encapsulation: control stock changes
    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self.__quantity = value

    def stock_value(self):
        return self.__price * self.__quantity

    def sell(self, amount):
        if amount <= 0:
            raise ValueError("Enter a quantity greater than zero.")
        if amount > self.__quantity:
            raise ValueError("Not enough stock available.")

        self.__quantity -= amount

    def restock(self, amount):
        if amount <= 0:
            raise ValueError("Enter a quantity greater than zero.")

        self.__quantity += amount


# Inheritance: Electronics inherits Product
class Electronics(Product):
    def __init__(self, product_id, name, price, quantity):
        super().__init__(
            product_id, name, price, quantity, "Electronics"
        )


# Inheritance: Grocery inherits Product
class Grocery(Product):
    def __init__(self, product_id, name, price, quantity):
        super().__init__(
            product_id, name, price, quantity, "Grocery"
        )
