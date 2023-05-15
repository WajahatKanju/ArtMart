from django.test import TestCase
from django.contrib.auth.models import Group
from .models import (
    User,
    Seller,
    SupportStaff,
    DeliveryPersonnel,
    AffiliatePartner,
    WholesaleBuyer,
    Manufacturer,
    Address,
)

from .forms import SignupForm

# Model Tests


class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            first_name="John",
            last_name="Doe",
            user_type="customer",
            phone_number="1234567890",
            gender="M",
            is_staff=True,
            is_superuser=False,
        )

        self.staff_user = User.objects.create(
            username="staffuser",
            user_type="support",
            phone_number="9876543210",
            gender="F",
        )
        self.staff_user.set_password("staffpassword")
        self.staff_user.save()

        self.admin_user = User.objects.create(
            username="adminuser",
            user_type="admin",
            phone_number="5555555555",
            gender="O",
        )
        self.admin_user.set_password("adminpassword")
        self.admin_user.save()

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 3)
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.get_full_name(), "John Doe")
        self.assertEqual(self.user.user_type, "customer")
        self.assertEqual(self.user.phone_number, "1234567890")
        self.assertEqual(self.user.gender, "M")
        self.assertTrue(self.user.check_password("testpassword"))
        self.assertTrue(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_staff_user_creation(self):
        self.assertEqual(self.staff_user.user_type, "support")
        self.assertTrue(self.staff_user.check_password("staffpassword"))

    def test_admin_user_creation(self):
        self.assertEqual(self.admin_user.user_type, "admin")
        self.assertTrue(self.admin_user.check_password("adminpassword"))

    def test_staff_user_permissions(self):
        staff_group = Group.objects.get(name="Staff")
        self.staff_user.groups.add(staff_group)

        # Test if the staff user has the required permissions
        self.assertTrue(self.staff_user.has_perm("accounts.change_user"))
        self.assertTrue(self.staff_user.has_perm("accounts.view_user"))
        self.assertFalse(self.staff_user.has_perm("accounts.add_user"))
        self.assertFalse(self.staff_user.has_perm("accounts.delete_user"))

    def test_admin_user_permissions(self):
        admin_group = Group.objects.get(name="Admin")
        self.admin_user.groups.add(admin_group)

        # Test if the admin user has the required permissions
        self.assertTrue(self.admin_user.has_perm("accounts.add_user"))
        self.assertTrue(self.admin_user.has_perm("accounts.change_user"))
        self.assertTrue(self.admin_user.has_perm("accounts.delete_user"))
        self.assertTrue(self.admin_user.has_perm("accounts.view_user"))


class SellerModelTestCase(TestCase):
    def setUp(self):
        self.seller = Seller.objects.create(
            username="testseller",
            user_type="seller",
            phone_number="9876543210",
            gender="F",
            shop_name="Test Shop",
        )

    def test_seller_creation(self):
        self.assertEqual(Seller.objects.count(), 1)
        self.assertEqual(self.seller.username, "testseller")
        self.assertEqual(self.seller.user_type, "seller")
        self.assertEqual(self.seller.phone_number, "9876543210")
        self.assertEqual(self.seller.gender, "F")
        self.assertEqual(self.seller.shop_name, "Test Shop")


class SupportStaffModelTestCase(TestCase):
    def setUp(self):
        self.support_staff = SupportStaff.objects.create(
            username="teststaff",
            user_type="support",
            phone_number="1234567890",
            gender="M",
            department="Support Department",
        )

    def test_support_staff_creation(self):
        self.assertEqual(SupportStaff.objects.count(), 1)
        self.assertEqual(self.support_staff.username, "teststaff")
        self.assertEqual(self.support_staff.user_type, "support")
        self.assertEqual(self.support_staff.phone_number, "1234567890")
        self.assertEqual(self.support_staff.gender, "M")
        self.assertEqual(self.support_staff.department, "Support Department")


class DeliveryPersonnelModelTestCase(TestCase):
    def setUp(self):
        self.delivery_personnel = DeliveryPersonnel.objects.create(
            username="testdelivery",
            user_type="delivery",
            phone_number="9876543210",
            gender="M",
            vehicle_type="Car",
            license_plate="ABC123",
        )

    def test_delivery_personnel_creation(self):
        self.assertEqual(DeliveryPersonnel.objects.count(), 1)
        self.assertEqual(self.delivery_personnel.username, "testdelivery")
        self.assertEqual(self.delivery_personnel.user_type, "delivery")
        self.assertEqual(self.delivery_personnel.phone_number, "9876543210")
        self.assertEqual(self.delivery_personnel.gender, "M")
        self.assertEqual(self.delivery_personnel.vehicle_type, "Car")
        self.assertEqual(self.delivery_personnel.license_plate, "ABC123")


class AffiliatePartnerModelTestCase(TestCase):
    def setUp(self):
        self.affiliate_partner = AffiliatePartner.objects.create(
            username="testaffiliate",
            user_type="affiliate",
            phone_number="9876543210",
            gender="F",
            website="https://example.com",
        )

    def test_affiliate_partner_creation(self):
        self.assertEqual(AffiliatePartner.objects.count(), 1)
        self.assertEqual(self.affiliate_partner.username, "testaffiliate")
        self.assertEqual(self.affiliate_partner.user_type, "affiliate")
        self.assertEqual(self.affiliate_partner.phone_number, "9876543210")
        self.assertEqual(self.affiliate_partner.gender, "F")
        self.assertEqual(self.affiliate_partner.website, "https://example.com")


class WholesaleBuyerModelTestCase(TestCase):
    def setUp(self):
        self.wholesale_buyer = WholesaleBuyer.objects.create(
            username="testwholesalebuyer",
            user_type="wholesale",
            phone_number="9876543210",
            gender="F",
            company_name="Example Wholesale",
            tax_number="1234567890",
        )

    def test_wholesale_buyer_creation(self):
        self.assertEqual(WholesaleBuyer.objects.count(), 1)
        self.assertEqual(self.wholesale_buyer.username, "testwholesalebuyer")
        self.assertEqual(self.wholesale_buyer.user_type, "wholesale")
        self.assertEqual(self.wholesale_buyer.phone_number, "9876543210")
        self.assertEqual(self.wholesale_buyer.gender, "F")
        self.assertEqual(self.wholesale_buyer.company_name, "Example Wholesale")
        self.assertEqual(self.wholesale_buyer.tax_number, "1234567890")


class ManufacturerModelTestCase(TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer.objects.create(
            username="testmanufacturer",
            user_type="manufacturer",
            phone_number="9876543210",
            gender="M",
            company_name="Example Company",
            address="123 Main St",
        )

    def test_manufacturer_creation(self):
        self.assertEqual(Manufacturer.objects.count(), 1)
        self.assertEqual(self.manufacturer.username, "testmanufacturer")
        self.assertEqual(self.manufacturer.user_type, "manufacturer")
        self.assertEqual(self.manufacturer.phone_number, "9876543210")
        self.assertEqual(self.manufacturer.gender, "M")
        self.assertEqual(self.manufacturer.company_name, "Example Company")
        self.assertEqual(self.manufacturer.address, "123 Main St")


class AddressModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            user_type="customer",
            phone_number="1234567890",
            gender="M",
        )
        self.address = Address.objects.create(
            user=self.user,
            address="123 Test St",
            country_id=1,
            state_id=1,
            city_id=1,
            postal_code="12345",
            address_type="Billing",
        )

    def test_address_creation(self):
        self.assertEqual(Address.objects.count(), 1)
        self.assertEqual(self.address.user, self.user)
        self.assertEqual(self.address.address, "123 Test St")
        self.assertEqual(self.address.country_id, 1)
        self.assertEqual(self.address.state_id, 1)
        self.assertEqual(self.address.city_id, 1)
        self.assertEqual(self.address.postal_code, "12345")
        self.assertEqual(self.address.address_type, "Billing")


# Form Tests


class SignupFormTestCase(TestCase):
    def test_form_valid(self):
        form_data = {
            "username": "testuser",
            "password1": "testpassword",
            "password2": "testpassword",
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@example.com",
            "phone_number": "9876543210",
            "date_of_birth": "1990-01-01",
            "gender": "M",
        }
        form = SignupForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {
            "username": "testuser",
            "password1": "testpassword",
            "password2": "differentpassword",
            "first_name": "John",
            "last_name": "Doe",
            "email": "invalid_email",
            "phone_number": "1234567890",
            "date_of_birth": "1990-01-01",
            "gender": "X",
        }
        form = SignupForm(data=form_data)
        self.assertFalse(form.is_valid())
