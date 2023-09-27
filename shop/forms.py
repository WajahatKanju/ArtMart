from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from orders.constants import PaymentMethod
from users.models import Customer


class CustomPasswordInput(forms.PasswordInput):
    def render(self, name, value, attrs=None, renderer=None):
        # Add custom rendering here
        output = super().render(name, value, attrs, renderer)
        return output


class CustomerSignInForm(forms.Form):
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

    bank_name = forms.CharField()
    bank_account_number = forms.CharField()
    payment_preferences = forms.ChoiceField(
        choices=PaymentMethod.choices,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(Column("first_name"), Column("last_name")),
            Row(Column("email"), Column("phone")),
            Row(Column("password1"), Column("password2")),
            Row(
                Column("bank_name"),
                Column("bank_account_number"),
                Column("payment_preferences"),
            ),
            Submit("submit", "Submit", css_class="button white"),
        )

    def save(self, user, *args, **kwargs):
        Customer.objects.get_or_create(user=user)


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        label="Password",
        widget=CustomPasswordInput(
            attrs={
                "autocomplete": "new-password",
                "required": True,
                "id": "id_password1",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(Column("email"), Column("password")),
            Submit("submit", "Submit", css_class="button white"),
        )

    def save(self, user, *args, **kwargs):
        pass
