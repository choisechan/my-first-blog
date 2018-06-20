from django.contrib import admin
from .models import gudok_Album , gudok_Item
# Register your models here.
class gudok_AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

class gudok_ItemAdmin(admin.ModelAdmin):
    list_display = ('album', 'origin','upload_date','Subscription_ratings','purchase_after_sub','owner')

admin.site.register(gudok_Album, gudok_AlbumAdmin)
admin.site.register(gudok_Item, gudok_ItemAdmin)
