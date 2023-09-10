from django import forms
from .models import Seller
from django.utils.translation import gettext_lazy as _

from .constants import PaymentPreference


class SellerAdminForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = "__all__"  # Include all fields from the Seller model

    # Include fields from the related User model
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    is_staff = forms.BooleanField()
    is_active = forms.BooleanField()

    bank_name = forms.CharField()
    bank_account_number = forms.CharField()
    payment_preferences = forms.ChoiceField(
        choices=PaymentPreference.choices,
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"})
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
