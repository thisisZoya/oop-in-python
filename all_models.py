class User:
    def __init__(self, username, password, fullname, email):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email

    def check_password(self, password):
        self.password = password

    @classmethod    # class method is a method that is bound to the class and not the instance of the class. 
                    # it need cls as a parameter.
                    # it dose not initiate any instance or class variable.
    def create(cls,username, password, fullname, email):
        cls.validate_password(password)
        return cls(username, password, fullname, email)

    @staticmethod   # static method is a method that is not bound to the class or instance of the class.
                    # it dose not need self or cls as a parameter.
                    # it dose not initiate any instance or class variable.
    def  validate_password(password):
        if len(password) < 3:
            print("password is too short")
            return False
        return True

    def __str__(self):
        return self.username

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

    @property
    def wallet(self):   # convert method to attribute.  
        return self.wallet_amount
        
class Reseller(User):
    def __init__(self, brand, log, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def check_password(self, password):
        print("login is not available")
        

class Product:
    product_list = list()  # class varible 
    
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
