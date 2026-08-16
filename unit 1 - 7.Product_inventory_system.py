class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def categorize(self):
        if self.price >= 1000:
            return "Expensive"
        else:
            return "Affordable"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print("\n--- Product Inventory ---")
        for product in self.products:
            print("Product ID:", product.product_id)
            print("Product Name:", product.product_name)
            print("Price:", product.price)
            print("Category:", product.categorize())
            print()


# Creating Inventory object
inventory = Inventory()

# Adding products
p1 = Product(101, "Laptop", 55000)
p2 = Product(102, "Mouse", 500)
p3 = Product(103, "Keyboard", 1500)

inventory.add_product(p1)
inventory.add_product(p2)
inventory.add_product(p3)

# Display all products
inventory.display_products()
