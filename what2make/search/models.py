from __future__ import unicode_literals

from django.db import models


# saved web-sites
class Site(models.Model):
    name = models.CharField(max_length=200)

# types of ingredients
class IngredientType(models.Model):
    type_name = models.CharField(max_length=200)

# ingredients
class Ingredient(models.Model):
    ing_name = models.CharField(max_length=200)
    type_name = models.ForeignKey(IngredientType, on_delete=models.CASCADE,)

# saved recipes
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE,)
    ingredients = models.ManyToManyField(Ingredient)

# users
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    recipes = models.ManyToManyField(Recipe)
    blocked_ingredients = models.ManyToManyField(Ingredient)
