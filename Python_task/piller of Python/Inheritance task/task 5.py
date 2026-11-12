class Product:
    def __init__(self):
        self.product_name="Laptop"
        self.price="85000"
    def display_product(self):
        print("\nProduct Name:",self.product_name)
        print("Product Price:",self.price)    

class Electronics(Product):
    def __init__(self):
        Product.__init__(self)
        self.warranty="1 years"
    def display_warranty(self):
        print("Product Warenty:",self.warranty)

    def check_warranty(self):
        print("The waranty is avaliable: 2 years, 4 years")


class Clothing(Product):
    def __init__(self):
        Product.__init__(self)
        self.size="XL"
    def display_size(self):
        print("Size:",self.size)
    def check_size(self):
        print("Avaliable size: L,M,XS,XL,XXL")

e=Electronics()
c=Clothing()
e.display_product()
e.display_warranty()
e.check_warranty()

c.display_product()
c.display_size()
c.check_size()
