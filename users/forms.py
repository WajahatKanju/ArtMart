from django import forms
from .models import Seller, Customer

from .constants import PaymentPreference


class CustomPasswordInput(forms.PasswordInput):
    def render(self, name, value, attrs=None, renderer=None):
        # Add custom rendering here
        output = super().render(name, value, attrs, renderer)
        return output


class SellerAdminForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = "__all__"  # Include all fields from the Seller model

    # Include fields from the related User model
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(
        label="Password",
        widget=CustomPasswordInput(
            attrs={
                "autocomplete": "new-password",
                "required": True,
                "id": "id_password1",
            }
        ),
        help_text=(
            "Your password can't be too similar to your other personal information.<br>"
            "Your password must contain at least 8 characters.<br>"
            "Your password can't be a commonly used password.<br>"
            "Your password can't be entirely numeric."
        ),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=CustomPasswordInput(
            attrs={
                "autocomplete": "new-password",
                "required": True,
                "id": "id_password2",
            }
        ),
    )
    phone = forms.CharField()
    is_staff = forms.BooleanField()
    is_active = forms.BooleanField()

    bank_name = forms.CharField()
    bank_account_number = forms.CharField()
    payment_preferences = forms.ChoiceField(
        choices=PaymentPreference.choices,
    )


class CustomerAdminForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"  # Include all fields from the Seller model

    # Include fields from the related User model
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(
        label="Password",
        widget=CustomPasswordInput(
            attrs={
                "autocomplete": "new-password",
                "required": True,
                "id": "id_password1",
            }
        ),
        help_text=(
            "Your password can't be too similar to your other personal information.<br>"
            "Your password must contain at least 8 characters.<br>"
            "Your password can't be a commonly used password.<br>"
            "Your password can't be entirely numeric."
        ),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=CustomPasswordInput(
            attrs={
                "autocomplete": "new-password",
                "required": True,
                "id": "id_password2",
            }
        ),
    )
    phone = forms.CharField()
    is_staff = forms.BooleanField()
    is_active = forms.BooleanField()

    bank_name = forms.CharField()
    bank_account_number = forms.CharField()
    payment_preferences = forms.ChoiceField(
        choices=PaymentPreference.choices,
    )
