from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django.utils import timezone
from photo.fields import ThumbnailImageField

from django.contrib.auth.models import User
# Create your models here.


@python_2_unicode_compatible
class gudok_Album(models.Model):
    name = models.CharField(max_length=50)
    category = models.IntegerField(default=4)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class gudok_Item(models.Model):
    album = models.ForeignKey(gudok_Album, null=True )
    #한 줄 설명
    origin = models.CharField(max_length=50)
    #image = ThumbnailImageField(upload_to='photo/%Y/%m')
    #description = models.TextField('상세설명', blank=True)
    upload_date = models.DateTimeField('Upload Date', auto_now_add=True)
    #cnt = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    Subscription_ratings=models.IntegerField(default=0)
    purchase_after_sub=models.IntegerField(default=0)
    owner = models.ForeignKey(User, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.album
