
from functools import partial

from django import forms

# from registrations.models import *

from .models import *
# from public_sector .models import *

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('symptoms', )


class SubscriptionCategoryForm(forms.ModelForm):
    class Meta:
        model = SubscriptionCategory
        fields = ('name', 'description', 'price', 'duration_days')


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('payment_method', 'amount')
