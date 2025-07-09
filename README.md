# oop-in-python
# 🐍 Practice Project: Exploring OOP Concepts in Python

This project is a hands-on exercise for learning and implementing core Object-Oriented Programming (OOP) principles in Python. The code establishes a basic structure for managing users and products in a hypothetical system.

---

## 🎯 Core Concepts Implemented

This project covers the following key concepts:

* **Class & Object:**
    The foundation of the program is built by defining classes like `User`, `Customer`, `Reseller`, and `Product`, from which different objects can be created.

* **Inheritance:**
    The `Customer` and `Reseller` classes inherit from the `User` class, gaining all of its attributes and methods. This prevents code duplication.
    ```python
    class Customer(User):
        pass
    ```

* **Method Overriding:**
    The `Reseller` class overrides the `check_password` method from its parent class, changing its behavior.

* **Constructor (`__init__`) & `super()`:**
    Each class has an `__init__` method to initialize an object's attributes. The `super()` function is used to call the parent class's constructor from within a child class.

* **Class Variables:**
    Class variables are used to share data among all instances of a class, such as `product_list` in the `Product` class, which keeps a list of all created products.

* **`@classmethod`:**
    In the `User` class, the `@classmethod` decorator is used to create the `create` method. This method has access to the class itself (not a specific instance) and can perform operations like validation before creating an object.

* **`@staticmethod`:**
    The `validate_password` method in the `User` class is defined as a static method. It's a utility function that doesn't depend on the class or its instances but is placed inside the class for logical grouping.

* **`@property`:**
    In the `Customer` class, the `@property` decorator is used for the `wallet` method. This allows us to access the method as if it were a regular attribute (without parentheses), improving code readability.
    ```python
    # Instead of customer1.wallet(), we write:
    print(customer1.wallet)
    ```

* **Special Methods:**
    The `__str__` method is used to define a user-friendly string representation of objects, so they provide meaningful output when printed.

---

## 🚀 How to Use

This code is designed as a module. You can import the classes and instantiate them:

```python
# Create a new user with the classmethod
user1 = User.create('zoya', 'pass123', 'Zoya Hussain', 'zoya@example.com')

# Create a product
product1 = Product(upc="12345", name="Laptop", price=1200)

# Display information
print(user1)
print(product1)

# Access the property
# customer1 = Customer(...)
# print(customer1.wallet)