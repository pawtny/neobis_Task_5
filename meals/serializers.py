from rest_framework import serializers
from .models import Department, MealCategory, Meal

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"
    
class MealCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = MealCategory
        fields = "__all__"
    
class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = "__all__"
