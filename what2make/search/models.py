from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# ingredient type model
class Ing_Type(models.Model):
    name = models.CharField(max_length=10)

# ingredient model
class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    ing_type = models.ForeignKey(Ing_Type, on_delete=models.CASCADE)
    cost = models.PositiveSmallIntegerField()

# recipes model
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    ingredients = models.ManyToManyField(Ingredient)

# user profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved = models.ManyToManyField(Recipe)
    blocked = models.ManyToManyField(Ingredient)

# rating model
class Rating(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
