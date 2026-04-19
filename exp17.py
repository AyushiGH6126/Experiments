class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        if product.stock >= quantity:
            self.items.append((product, quantity))
            product.stock -= quantity
        else:
            print("Not enough stock")

    def total_cost(self):
        total = sum(p.price * q for p, q in self.items)
        return total


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def checkout(self):
        print("Total Amount:", self.cart.total_cost())


# Example
p1 = Product("Laptop", 50000, 10)
c1 = Customer("Ayushi")

c1.cart.add_item(p1, 2)
c1.checkout()