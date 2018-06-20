from photo.models import Album, Photo
from django.forms.models import inlineformset_factory

PhotoInlineFormSet = inlineformset_factory(Album, Photo,
    fields = ['image', 'origin', 'description','cnt','price' ,'Subscription_ratings','purchase_after_sub'],
    extra = 2)
