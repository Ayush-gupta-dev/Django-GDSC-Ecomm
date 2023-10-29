from django.contrib import admin



# Register your models here.

from .models import Category, Item,PriorityTag

admin.site.register(Category)
admin.site.register(PriorityTag)
admin.site.register(Item)