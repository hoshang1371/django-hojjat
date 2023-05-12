from django import forms

from post_information.models import PostAddress

class UserPostAddressDetailForm(forms.Form):

    # CHOICES = [('1', 'First'), ('2', 'Second'), ('3', 'three')]

    PostAddress_id = forms.ChoiceField(
        widget=forms.RadioSelect,
        # choices= CHOICES
    )
    
    # isResive = forms.BooleanField(
    #     # widget=forms.HiddenInput(),
    #     initial=True
    #     )
    
    def __init__(self, *args, **kwargs):
        user =args[1]
        postAddressesUser = PostAddress.objects.filter(owner_id=user.id)
        # postAddressesUser = PostAddress.objects.filter(owner_id=14)
        self.choices = []
        for p in postAddressesUser:
            t = (str(p.id),p.address)
            self.choices.append(t)
        super(UserPostAddressDetailForm, self).__init__(*args, **kwargs)
        self.fields['PostAddress_id'].choices =self.choices
        
