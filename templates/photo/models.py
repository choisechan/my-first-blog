from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.core.urlresolvers import reverse

from photo.fields import ThumbnailImageField

from django.contrib.auth.models import User

# Create your models here.

@python_2_unicode_compatible
class Album(models.Model):
    name = models.CharField(max_length=50)
    category = models.IntegerField(default=4)
    description = models.CharField('One Line Description', max_length=100, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))

@python_2_unicode_compatible
class Photo(models.Model):
    album = models.ForeignKey(Album)
    #한 줄 설명
    origin = models.CharField(max_length=50)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    description = models.TextField('상세설명', blank=True)
    upload_date = models.DateTimeField('Upload Date', auto_now_add=True)
    cnt = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    Subscription_ratings=models.CharField(max_length=50)
    purchase_after_sub=models.CharField(max_length=50)
    owner = models.ForeignKey(User, null=True)




    class Meta:
        ordering = ['origin']

    def __str__(self):
        return self.origin

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))
