from django.test import TestCase
from store.models import Category, Customer, Order, Product

# Test case for Category model
class CategoryTest(TestCase):

    def setUp(self):
        # Create a Category instance to use in tests
        self.category = Category.objects.create(name='Test Category')

    def test_category_name(self):
        # Test to ensure the category name is correctly assigned
        self.assertEqual(self.category.name, 'Test Category')

    def test_get_all_categories(self):
        # Test to ensure that Category is saved and retrieved correctly
        categories = Category.objects.all()
        self.assertEqual(categories.count(), 1)
        self.assertEqual(categories[0].name, 'Test Category')

# Test case for Customer model
class CustomerTest(TestCase):

    def setUp(self):
        # Create a Customer instance
        self.customer = Customer.objects.create(first_name='John', last_name='Doe', email='john.doe@example.com')

    def test_customer_full_name(self):
        # Test to check if full name is generated correctly
        self.assertEqual(self.customer.first_name, 'John')
        self.assertEqual(self.customer.last_name, 'Doe')

    def test_get_customer_by_email(self):
        # Test customer retrieval using email
        customer_by_email = Customer.objects.get(email='john.doe@example.com')
        self.assertEqual(customer_by_email.first_name, 'John')

class OrderTest(TestCase):

    def setUp(self):
        # Create a Customer instance
        self.customer = Customer.objects.create(first_name='John', last_name='Doe', email='john.doe@example.com')

    def test_customer_full_name(self):
        # Test to check if full name is generated correctly
        self.assertEqual(self.customer.first_name, 'John')
        self.assertEqual(self.customer.last_name, 'Doe')

    def test_get_customer_by_email(self):
        # Test customer retrieval using email
        customer_by_email = Customer.objects.get(email='john.doe@example.com')
        self.assertEqual(customer_by_email.first_name, 'John')























'''
# Test case for Order model
class OrderTest(TestCase):

    def setUp(self):
        # Create Category and Customer instances manually
        self.category = Category.objects.create(name='Test Category')
        self.customer = Customer.objects.create(first_name='John', last_name='Doe', email='john.doe@example.com')

        # Create Product instances linked to the category
        self.product1 = Product.objects.create(name='Product 1', category=self.category, price=100.0)
        self.product2 = Product.objects.create(name='Product 2', category=self.category, price=200.0)

        # Explicitly assign ForeignKey relationships
        self.order = Order.objects.create(customer=self.customer, category=self.category)

    def test_place_order(self):
        # Test if the Order is correctly created with customer and category
        order = Order.objects.get(id=self.order.id)
        self.assertEqual(order.customer.first_name, 'John')
        self.assertEqual(order.category.name, 'Test Category')

    def test_get_orders_by_customer(self):
        # Fetch all orders for a specific customer
        orders = Order.objects.filter(customer=self.customer)
        self.assertEqual(orders.count(), 1)

    def test_get_all_products_by_categoryid(self):
        # Retrieve all products linked to the category
        products = Product.objects.filter(category=self.category)

        # Ensure that the correct products are retrieved
        self.assertEqual(products.count(), 2)  # Two products were created in setUp
        self.assertEqual(products[0].name, 'Product 1')
        self.assertEqual(products[1].name, 'Product 2')
'''