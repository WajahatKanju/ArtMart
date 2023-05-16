from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Order, OrderItem, Payment
from products.models import Product

User = get_user_model()


class OrderTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            email="test@example.com",
        )
        self.order = Order.objects.create(
            user=self.user,
            total_price=100.00,
        )

    def test_order_creation(self):
        self.assertEqual(
            str(self.order), f"Order #{self.order.id} by {self.user.username}"
        )
        self.assertEqual(self.order.total_price, 100.00)
        self.assertEqual(self.order.shipping_address, None)

    def test_order_user_relationship(self):
        self.assertEqual(self.order.user, self.user)
        self.assertIn(self.order, self.user.orders.all())


class OrderItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.user = User.objects.create(username="testuser")
        cls.order = Order.objects.create(user=cls.user, total_price=100.00)
        cls.product = Product.objects.create(
            name="Test Product", price=10.00, stock_quantity=10
        )

        cls.order_item = OrderItem.objects.create(
            order=cls.order, product=cls.product, quantity=2
        )

    def test_order_item_creation(self):
        order_item = OrderItem.objects.get(id=self.order_item.id)
        self.assertEqual(order_item.order, self.order)
        self.assertEqual(order_item.product, self.product)
        self.assertEqual(order_item.quantity, 2)

    def test_order_item_string_representation(self):
        expected_string = "2 x Test Product"
        self.assertEqual(str(self.order_item), expected_string)


class PaymentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            email="test@example.com",
        )
        self.payment = Payment.objects.create(
            user=self.user,
            amount=50.00,
        )

    def test_payment_creation(self):
        payment = Payment.objects.get(id=self.payment.id)
        self.assertEqual(payment.user, self.user)
        self.assertEqual(payment.amount, 50.00)

    def test_payment_string_representation(self):
        expected_string = f"Payment by {self.user.username} - $50.0"
        self.assertEqual(str(self.payment), expected_string)
