from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import transaction
from django.contrib.auth.hashers import make_password
from .models import Seller, User
from .forms import SellerAdminForm


@receiver(pre_save, sender=Seller)
def create_user_for_seller(sender, instance, **kwargs):
    if instance.user_id is None:
        # Create a new User instance only if it doesn't already exist
        user = User(
            email=instance.email,
            first_name=instance.first_name,
            last_name=instance.last_name,
            is_staff=instance.is_staff,
            is_active=instance.is_active,
            bank_name=instance.bank_name,
            bank_account_number=instance.bank_account_number,
            payment_preferences=instance.payment_preferences,
            phone=instance.phone,
            # You can set other fields here
        )

        # Set the user's password using make_password
        user.password = make_password(instance.password)

        # Use a transaction to ensure both user and seller are saved or none
        with transaction.atomic():
            user.save()
            instance.user = user  # Associate the user with the seller
