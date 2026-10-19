
from product import Product


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        for item in self.products:
            if item.product_id == product.product_id:
                raise ValueError("Product ID already exists.")

        self.products.append(product)

    def find_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def sell_product(self, product_id, amount):
        product = self.find_product(product_id)

        if product is None:
            raise ValueError("Product not found.")

        product.sell(amount)

    def restock_product(self, product_id, amount):
        product = self.find_product(product_id)

        if product is None:
            raise ValueError("Product not found.")

        product.restock(amount)

    def total_stock_value(self):
        return sum(p.stock_value() for p in self.products)

    def low_stock_products(self):
        return [p for p in self.products if p.quantity <= 5]
