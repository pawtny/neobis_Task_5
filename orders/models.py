from django.db import models
from meals.models import Meal
from users.models import User

class ServicePercentage(models.Model):
    percentage = models.IntegerField("percentage for the service", null = False)

    def __str__(self):
        return str(self.percentage)


class Status(models.Model):
    name = models.CharField("name of the status", max_length = 50)

    def __str__(self):
        return self.name

class Table(models.Model):
    name = models.CharField("name of the table", max_length = 50)

    def __str__(self):
        return self.name


class Order(models.Model):
    waiterid = models.ForeignKey(User, related_name='orders', null = True, on_delete = models.CASCADE)
    tableid = models.ForeignKey(Table, null = True, on_delete = models.SET_NULL)
    isitopen = models.BooleanField(default=True)
    date = models.DateTimeField("date of creation", auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)


class OneMealToOrder(models.Model):
    orderid = models.ForeignKey(Order, related_name='meals', on_delete=models.CASCADE)
    mealid = models.ForeignKey(Meal, related_name='mealsid', on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField()

    def getSum(self):
        return self.count * Meal.objects.get(id=self.mealid.id).price

    def __str__(self):
        return str(self.orderid.id)


class Check(models.Model):
    orderid = models.ForeignKey(Order, related_name='checks', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def totalSum(self):
        return sum([e.getSum() for e in OneMealToOrder.objects.filter(orderid=self.orderid)]) + ServicePercentage.objects.latest('id').percentage

    def __str__(self):
        return str(self.orderid)