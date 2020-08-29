from django.db import models
from django.core.validators import MinValueValidator

class Department(models.Model):
    name = models.CharField("name of the department", max_length = 50, unique = True)

class MealCategory(models.Model):
    name = models.CharField("name of the category", max_length = 50, unique = True)
    departmentid = models.ForeignKey(Department, on_delete = models.CASCADE)

class Meal(models.Model):
    name = models.CharField("name of the meal", max_length = 80)
    categoryid = models.ForeignKey(MealCategory, null = True, on_delete = models.SET_NULL)
    price = models.PositiveIntegerField("price of the meal", validators=[MinValueValidator(1)])
    description = models.TextField("description of a meal", blank = True, default = "")

