from django.test import TestCase
from products.models import (
    Product,
    ProductImage,
    AttributeType,
    Attribute,
    Brand,
    Category,
    Cart,
    CartItem,
    Review,
)
from mptt.exceptions import InvalidMove
from django.contrib.auth import get_user_model

User = get_user_model()


class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="This is a test product",
            price=10.00,
            stock_quantity=50,
        )

    def test_product_creation(self):
        product = Product.objects.get(id=self.product.id)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "This is a test product")
        self.assertEqual(product.price, 10.00)
        self.assertEqual(product.stock_quantity, 50)

    def test_product_string_representation(self):
        expected_string = "Test Product"
        self.assertEqual(str(self.product), expected_string)


class ProductImageModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product")
        self.product_image = ProductImage.objects.create(
            product=self.product,
            image="path/to/image.jpg",
        )

    def test_product_image_creation(self):
        product_image = ProductImage.objects.get(id=self.product_image.id)
        self.assertEqual(product_image.product, self.product)
        self.assertEqual(product_image.image, "path/to/image.jpg")

    def test_product_image_string_representation(self):
        expected_string = "Image for Test Product"
        self.assertEqual(str(self.product_image), expected_string)


class AttributeTypeModelTest(TestCase):
    def setUp(self):
        self.attribute_type = AttributeType.objects.create(name="Size")

    def test_attribute_type_creation(self):
        attribute_type = AttributeType.objects.get(id=self.attribute_type.id)
        self.assertEqual(attribute_type.name, "Size")

    def test_attribute_type_string_representation(self):
        expected_string = "Size"
        self.assertEqual(str(self.attribute_type), expected_string)


class AttributeModelTest(TestCase):
    def setUp(self):
        self.attribute_type = AttributeType.objects.create(name="Size")
        self.attribute = Attribute.objects.create(
            name="Small",
            attribute_type=self.attribute_type,
        )

    def test_attribute_creation(self):
        attribute = Attribute.objects.get(id=self.attribute.id)
        self.assertEqual(attribute.name, "Small")
        self.assertEqual(attribute.attribute_type, self.attribute_type)

    def test_attribute_string_representation(self):
        expected_string = "Small"
        self.assertEqual(str(self.attribute), expected_string)


class BrandModelTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name="Nike")

    def test_brand_creation(self):
        brand = Brand.objects.get(id=self.brand.id)
        self.assertEqual(brand.name, "Nike")
        self.assertFalse(brand.top)

    def test_brand_string_representation(self):
        expected_string = "Nike"
        self.assertEqual(str(self.brand), expected_string)


class CategoryModelTest(TestCase):
    def setUp(self):
        self.root_category = Category.objects.create(name="Root Category")
        self.child_category = Category.objects.create(
            name="Child Category", parent=self.root_category
        )

    def test_category_creation(self):
        category = Category.objects.get(id=self.root_category.id)
        self.assertEqual(category.name, "Root Category")
        self.assertIsNone(category.parent)
        self.assertEqual(category.children.count(), 1)

    def test_category_string_representation(self):
        expected_string = "Root Category"
        self.assertEqual(str(self.root_category), expected_string)

    def test_category_relationship(self):
        self.assertEqual(self.child_category.parent, self.root_category)
        self.assertIn(self.child_category, self.root_category.children.all())

    def test_category_move(self):
        new_parent_category = Category.objects.create(name="New Parent Category")
        self.child_category.parent = new_parent_category
        self.child_category.save()
        self.assertEqual(self.child_category.parent, new_parent_category)
        self.assertIn(self.child_category, new_parent_category.children.all())

    def test_invalid_category_move(self):
        with self.assertRaises(InvalidMove):
            self.root_category.parent = self.child_category
            self.root_category.save()


class CartModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.cart = Cart.objects.create(user=self.user)

    def test_cart_creation(self):
        cart = Cart.objects.get(id=self.cart.id)
        self.assertEqual(str(cart), f"Cart for {self.user.username}")
        self.assertEqual(cart.user, self.user)
        self.assertEqual(cart.products.count(), 0)

    def test_cart_item_creation(self):
        product = Product.objects.create(name="Test Product", price=10.00)
        cart_item = CartItem.objects.create(cart=self.cart, product=product, quantity=2)
        self.assertEqual(str(cart_item), "2 x Test Product in Cart")
        self.assertEqual(cart_item.cart, self.cart)
        self.assertEqual(cart_item.product, product)
        self.assertEqual(cart_item.quantity, 2)

    def test_cart_item_relationship(self):
        product = Product.objects.create(name="Test Product", price=10.00)
        cart_item = CartItem.objects.create(cart=self.cart, product=product, quantity=2)
        self.assertEqual(cart_item.cart, self.cart)
        self.assertEqual(cart_item.product, product)
        self.assertIn(cart_item, self.cart.cartitem_set.all())

    def test_cart_item_quantity_update(self):
        product = Product.objects.create(name="Test Product", price=10.00)
        cart_item = CartItem.objects.create(cart=self.cart, product=product, quantity=2)
        cart_item.quantity = 3
        cart_item.save()
        self.assertEqual(cart_item.quantity, 3)


class CartItemModelTest(TestCase):
    def setUp(self):
        self.cart = Cart.objects.create()
        self.product = Product.objects.create(name="Test Product", price=10.00)
        self.cart_item = CartItem.objects.create(
            cart=self.cart, product=self.product, quantity=2
        )

    def test_cart_item_creation(self):
        cart_item = CartItem.objects.get(id=self.cart_item.id)
        self.assertEqual(str(cart_item), "2 x Test Product in Cart")
        self.assertEqual(cart_item.cart, self.cart)
        self.assertEqual(cart_item.product, self.product)
        self.assertEqual(cart_item.quantity, 2)

    def test_cart_item_quantity_update(self):
        self.cart_item.quantity = 3
        self.cart_item.save()
        updated_cart_item = CartItem.objects.get(id=self.cart_item.id)
        self.assertEqual(updated_cart_item.quantity, 3)


class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.product = Product.objects.create(name="Test Product", price=10.00)
        self.review = Review.objects.create(
            user=self.user,
            product=self.product,
            rating=4,
            comment="This is a great product!",
        )

    def test_review_creation(self):
        review = Review.objects.get(id=self.review.id)
        self.assertEqual(
            str(review), f"Review by {self.user.username} on {self.product.name}"
        )
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.product, self.product)
        self.assertEqual(review.rating, 4)
        self.assertEqual(review.comment, "This is a great product!")

    def test_review_str_representation(self):
        expected_string = f"Review by {self.user.username} on {self.product.name}"
        self.assertEqual(str(self.review), expected_string)
