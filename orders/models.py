from django.db import models
# from meals.models import Meal
# from users.models import User

class ServicePercentage(models.Model):
    percentage = models.IntegerField("percentage for the service", null = False, unique = True, primary_key = True)

class Status(models.Model):
    name = models.CharField("name of the status", max_length = 50)

class Table(models.Model):
    name = models.CharField("name of the table", max_length = 50)

# class Order(models.Model):
#     waiterid = models.ForeignKey("id of the user", settings.AUTH_USER_MODEL, null = True, on_delete = models.SET_NULL)
#     tableid = models.ForeignKey("id of the table", Table, null = True, on_delete = models.SET_NULL)
#     tablename = models.ForeignKey("name of the table", Table, to_field = name, null = True, on_delete = models.SET_NULL)
#     isitopen
#     date
#     mealsid = models.ForeignKey("id of the meals", Meal, null = True, on_delete = models.SET_NULL)


