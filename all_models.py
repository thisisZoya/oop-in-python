class User:
    def __init__(self, username, password, fullname, email):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email
    def check_password(self, password):
        self.password = password

class Customer(User):
    conter = 0 #class variable
    def __init__(self, username, password, fullname, email):
        super().__init__(username, password, fullname, email)
        self.wallet_amount = 0
        self.is_enable = False
    
    def __str__(self):
        self.username

    def set_enable(self, is_enable):
        self.set_enable = True
        
class Reseller(User):
    def __init__(self, brand, log, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def check_password(self, password):
        print("login is not available")
        

class Product:
    product_list = list()
    
    def __init__(self, upc, name, price=0, description='', reseller=None):
        self.upc = upc
        self.name = name
        self.price = price
        self.description = description
        Product.product_list.append(self)

    def __str__(self):
        return f"upc {self.upc} \t name: {self.name}"

    def is_free(self):
        return self.price == 0
