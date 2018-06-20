from django import forms

from .models import gudok_Item, gudok_Album

class gudok_ItemForm(forms.ModelForm):

    class Meta:
        model = gudok_Item
        fields = ('album', 'origin', 'price','Subscription_ratings','purchase_after_sub','owner')
