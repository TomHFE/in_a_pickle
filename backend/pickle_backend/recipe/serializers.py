from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Recipe 
        fields = [
        'username',
        'ingredients',
        'nationality',
        'preference',
        'dietaryRequirments',
        'created_at',
        'recipe'
        ]