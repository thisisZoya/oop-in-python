from all_models import *

if __name__ == "__main__":
    #create a customer
    c1 = Customer("user1", "123456", "John Doe", "john@example.com")
    c2 = Customer("user2", "123456", "Jane Doe", "jane@example.com")

c1.set_enable()
print(c1.username)

# create Product
p1 = Product("1", "product1")
p2 = Product("2", "product2", 100)
p3 = Product("3", "product3", 100, "description3")

c3 = Customer(email="user3@example.com", fullname="John Deo", password="123456", username="user3")

r1 = Reseller(
    "Brand1", "logo/path", "reseller1", "265", "reseller", "reseller@gmail.com"
)
print(r1.username, c3.username) 
print(type(r1), type(c3))

# reseller compoisition
P2 = Product(2, "Product2", 100, reseller=r1)
print(p2, p2.reseller.check_password(123)) 
print(type(p2), type(p2.reseller))
