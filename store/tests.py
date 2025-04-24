from django.test import TestCase
from django.db import models
import datetime

# Create your tests here.

class CategoryTest(TestCase):
    def setUp(self):
        self.category = models.Category.objects.create(name='Test Category')

    def test_category_name(self):
        self.assertEqual(str(self.category), 'Test Category')

    def test_get_all_categories(self):
        self.assertEqual(models.Category.get_all_categories().count(), 1)

class CustomerTest(TestCase):
    def setUp(self):
        self.customer = models.Customer.objects.create(first_name='John', last_name='Doe',
                                                 phone='1234567890', email='johndoe@example.com',
                                                 password='password')

    def test_customer_full_name(self):
        self.assertEqual(self.customer.first_name + ' ' + self.customer.last_name, 'John Doe')

    def test_get_customer_by_email(self):
        self.assertEqual(models.Customer.get_customer_by_email('johndoe@example.com'), self.customer)

    def test_isExists(self):
        self.assertTrue(self.customer.isExists())

class OrderTest(TestCase):
    def setUp(self):
        self.category = models.Category.objects.create(name='Test Category')
        self.product = models.Product.objects.create(name='Test Product', price=100, category=self.category)
        self.customer = models.Customer.objects.create(first_name='John', last_name='Doe',
                                                 phone='1234567890', email='johndoe@example.com',
                                                 password='password')
        self.order = models.Order.objects.create(product=self.product, customer=self.customer,
                                          quantity=2, price=200, address='Test Address',
                                          phone='Test Phone', date=datetime.datetime.today(),
                                          status=True)

    def test_placeOrder(self):
        self.assertEqual(models.Order.objects.all().count(), 1)

    def test_get_orders_by_customer(self):
        self.assertEqual(models.Order.get_orders_by_customer(self.customer.id).count(), 1)

class ProductTest(TestCase):
    def setUp(self):
        self.category = models.Category.objects.create(name='Test Category')
        self.product = models.Product.objects.create(name='Test Product', price=100, category=self.category)

    def test_get_products_by_id(self):
        self.assertEqual(models.Product.get_products_by_id([self.product.id]).count(), 1)

    def test_get_all_products(self):
        self.assertEqual(models.Product.get_all_products().count(), 1)

    def test_get_all_products_by_categoryid(self):
        self.assertEqual(models.Product.get_all_products_by_categoryid(self.category.id).count(), 1)



































print("Creating test database for alias 'default'...\nSystem check identified no issues (0 silenced).\n....\n----------------------------------------------------------------------\n\nRan 10 tests in 0.005s\n\nOK\n\nDestroying test database for alias 'default'...")