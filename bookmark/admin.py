from django.contrib import admin
from bookmark.models import *

# Register your models here.

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title','amount','photo', 'price','state','star','owner')

class SubGroupAdmin(admin.ModelAdmin):
    list_display = ('title','price')

class SubListAdmin(admin.ModelAdmin):
    list_display = ('title','price','owner')

admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(SubGroup, SubGroupAdmin)
admin.site.register(SubList, SubListAdmin)
