from rest_framework import serializers
from .models import Table, ServicePercentage, Status, Order, OneMealToOrder, Check
from meals.models import Meal

class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = "__all__"
    
class ServicePercentageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicePercentage
        fields = "__all__"
    
class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = "__all__"

class OneMealToOrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OneMealToOrder
        fields = ['mealid', 'count']

class OrderSerializer(serializers.ModelSerializer):
    waiterid = serializers.ReadOnlyField(source='waiterid.id')
    meals = OneMealToOrderSerializer(many = True)
    tablename = serializers.ReadOnlyField(source='tableid.name')

    class Meta:
        model = Order
        fields = ['id', 'waiterid', 'tableid', 'tablename', 'isitopen', 'date', 'meals']
    
    def create(self, validated_data):
        meals_data = validated_data.pop('meals')

        order = Order.objects.create(**validated_data)
        for meal_data in meals_data:
            OneMealToOrder.objects.create(orderid=order, **meal_data)

        return order

class MealsToOrderSerializer(serializers.Serializer):
    orderid = serializers.IntegerField(write_only=True)
    meals = OneMealToOrderSerializer(many = True)

    class Meta:
        model = Order
        fields = ['orderid', 'meals']

    def create(self, validated_data):
        meals_data = validated_data.pop('meals')
        order = Order.objects.get(pk=validated_data['orderid'])
        for meal_data in meals_data:
            OneMealToOrder.objects.create(orderid=order, **meal_data)
        return order



class CheckMealSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='orderid.mealsid.name')
    amount = serializers.ReadOnlyField(source='orderid.count')
    price = serializers.ReadOnlyField(source='orderid.mealsid.price')
    total = serializers.ReadOnlyField(source='orderid.getSum')
    test = "test"
    class Meta:
        model = OneMealToOrder
        fields = ['name', 'amount', 'price', 'total', 'test']


class CheckSerializer(serializers.ModelSerializer):
    meals = OneMealToOrderSerializer(many = True, read_only=True)

    class Meta:
        model = Check
        fields = ['id', 'orderid', 'date', 'meals']



