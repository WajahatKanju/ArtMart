from django import forms
from .models import (
    Seller,
    Customer,
    DeliveryDriver,
    Administrator,
    AffiliateMarketer,
    CustomerServiceRepresentative,
    MarketingManager,
    ProductManager,
    SocialMediaInfluencer,
    SalesRepresentative,
    LogisticsCoordinator,
    FinancialAnalyst,
    DataAnalyst,
    LegalCounsel,
    InventoryManager,
)
from .constants import Role
from orders.constants import PaymentMethod
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from crispy_forms.bootstrap import FormActions


class CustomPasswordInput(forms.PasswordInput):
    def render(self, name, value, attrs=None, renderer=None):
        # Add custom rendering here
        output = super().render(name, value, attrs, renderer)
        return output


class BaseAdminForm(forms.ModelForm):
    class Meta:
        abstract = True

    # Fields common to both Seller and Customer
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
    is_staff = forms.BooleanField(required=False)
    is_active = forms.BooleanField(required=False)
    bank_name = forms.CharField()
    bank_account_number = forms.CharField()
    payment_preferences = forms.ChoiceField(
        choices=PaymentMethod.choices,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                "Personal Information",
                "first_name",
                "last_name",
                "email",
                "password1",
                "password2",
                "phone",
            ),
            Fieldset(
                "User Permissions",
                "is_staff",
                "is_active",
            ),
            Fieldset(
                "Bank Information",
                "bank_name",
                "bank_account_number",
            ),
            Fieldset(
                "Payment Preferences",
                "payment_preferences",
            ),
            FormActions(Submit("submit", "Save Changes", css_class="btn-primary")),
        )


class SellerAdminForm(BaseAdminForm):
    class Meta:
        model = Seller
        fields = "__all__"  # Include all fields from the Seller model


class CustomerAdminForm(BaseAdminForm):
    class Meta:
        model = Customer
        fields = "__all__"  # Include all fields from the Customer model


class DeliveryDriverAdminForm(BaseAdminForm):
    class Meta:
        model = DeliveryDriver
        fields = "__all__"


class AdministratorAdminForm(BaseAdminForm):
    class Meta:
        model = Administrator
        fields = "__all__"


class AffiliateMarketerAdminForm(BaseAdminForm):
    class Meta:
        model = AffiliateMarketer
        fields = "__all__"

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = Role.AFFILIATE_MARKETER  # Set the role to Seller

        if commit:
            user.save()
        return user


class CustomerServiceRepresentativeAdminForm(BaseAdminForm):
    class Meta:
        model = CustomerServiceRepresentative
        fields = "__all__"


class MarketingManagerAdminForm(BaseAdminForm):
    class Meta:
        model = MarketingManager
        fields = "__all__"


class ProductManagerAdminForm(BaseAdminForm):
    class Meta:
        model = ProductManager
        fields = "__all__"


class SocialMediaInfluencerAdminForm(BaseAdminForm):
    class Meta:
        model = SocialMediaInfluencer
        fields = "__all__"


class SalesRepresentativeAdminForm(BaseAdminForm):
    class Meta:
        model = SalesRepresentative
        fields = "__all__"


class LogisticsCoordinatorAdminForm(BaseAdminForm):
    class Meta:
        model = LogisticsCoordinator
        fields = "__all__"


class FinancialAnalystAdminForm(BaseAdminForm):
    class Meta:
        model = FinancialAnalyst
        fields = "__all__"


class DataAnalystAdminForm(BaseAdminForm):
    class Meta:
        model = DataAnalyst
        fields = "__all__"


class LegalCounselAdminForm(BaseAdminForm):
    class Meta:
        model = LegalCounsel
        fields = "__all__"


class InventoryManagerAdminForm(BaseAdminForm):
    class Meta:
        model = InventoryManager
        fields = "__all__"
