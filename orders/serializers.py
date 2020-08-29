from rest_framework import serializers
from .models import Table, ServicePercentage, Status

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
