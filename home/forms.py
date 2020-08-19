from django.forms import (formset_factory, modelformset_factory)
from django import forms
from .models import *

class BillingForm(forms.ModelForm):
	rate = forms.IntegerField()
	class Meta:
		model = Billing
		fields = ['quantity','balance_amt','product','rate']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['product'].queryset = Product.objects.all()
		self.fields['product'].widget = forms.TextInput(attrs={
            'class': 'common-product'})
		self.fields['rate'].queryset = None

		if 'product' in self.data:
			try:
				product_id = int(self.data.get('pk'))
				self.fields['rate'] = Product.objects.get(pk=pk).values('rate')
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset


BillFormset = formset_factory(BillingForm, extra=1)