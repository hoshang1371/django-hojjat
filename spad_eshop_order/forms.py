from django import forms

class UserNewOrderForm(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput(),
    )

    count = forms.IntegerField(
        widget= forms.TextInput(attrs={'id':'numberProduct','value':'۱','class':'toPe'}),
        initial=1
    )