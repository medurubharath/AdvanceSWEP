from django.db import models

# Define the Category model
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Define the Customer model
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()  # Assuming you want to add email field for testing

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Define the Order model with ForeignKey to both Customer and Category
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # ForeignKey to Category
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} for {self.customer} in {self.category}"

# Define the Product model (added for completeness in tests)
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
