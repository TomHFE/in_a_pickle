from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Ingredients(models.Model):
  Ingredients_first = models.CharField(max_length=500, blank=True)
  Ingredients_second = models.CharField(max_length=500, blank=True)
  Ingredients_third = models.CharField(max_length=500, blank=True)
  Ingredients_fourth = models.CharField(max_length=500, blank=True)
  Ingredients_fifth = models.CharField(max_length=500, blank=True)
  Ingredients_sixth = models.CharField(max_length=500, blank=True)
  Ingredients_seventh = models.CharField(max_length=500, blank=True)
  Ingredients_eigth = models.CharField(max_length=500, blank=True)

  def __str__(self):
    return f'Ingredients {self.pk}'
  

class Recipe(models.Model):
   

  def validate_max_words(value):
      
      value = str(value)

      if value.strip() and len(value.split()) > 1000:
          raise ValidationError("Maximum word limit exceeded.")
    
  username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  ingredients = models.ForeignKey(Ingredients, on_delete=models.SET_NULL, null=True)
  nationality = models.CharField(max_length=200, blank=True)
  preference = models.TextField(validators=[validate_max_words], default='', blank=True)
  dietaryRequirments = models.TextField(validators=[validate_max_words], default='', blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  recipe = models.TextField(blank=True)


  def __str__(self):
    return f'{self.username}'
  


