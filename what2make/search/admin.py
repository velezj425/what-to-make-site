from django.contrib import admin

from .models import *

admin.site.register(Profile)
admin.site.register(Recipe)
admin.site.register(Ing_Type)
admin.site.register(Ingredient)