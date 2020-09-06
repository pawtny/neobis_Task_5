from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from .models import Table, ServicePercentage, Status, Order, Check
from .serializers import (TableSerializer, ServicePercentageSerializer, StatusSerializer, 
                            OrderSerializer, MealsToOrderSerializer, CheckSerializer)

class TableList(APIView):
    def get(self, request, format = None):
        tables = Table.objects.all()
        serializer = TableSerializer(tables, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TableDetails(APIView):
    def get_object(self, pk):
        try:
            return Table.objects.get(pk=pk)
        except Table.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def delete(self, request, pk, format=None):
        table = self.get_object(pk)
        table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StatusList(APIView):
    def get(self, request, format = None):
        statuses = Status.objects.all()
        serializer = StatusSerializer(statuses, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StatusDetails(APIView):
    def get_object(self, pk):
        try:
            return Status.objects.get(pk=pk)
        except Status.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def delete(self, request, pk, format=None):
        status = self.get_object(pk)
        status.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ServicePercentageList(APIView):
    def get(self, request, format = None):
        servicepercentage = ServicePercentage.objects.all()
        serializer = ServicePercentageSerializer(servicepercentage, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = ServicePercentageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServicePercentageDetails(APIView):
    def get_object(self, pk):
        try:
            return ServicePercentage.objects.get(pk=pk)
        except ServicePercentage.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def delete(self, request, pk, format=None):
        servicepercentage = self.get_object(pk)
        servicepercentage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format = None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(waiterid=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetails(APIView):
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def delete(self, request, pk, format=None):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActiveOrdersView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format = None):
        orders = Order.objects.filter(isitopen=True)
        serializer = OrderSerializer(orders, many = True)
        return Response(serializer.data)

class MealsToOrderView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk, format = None):
        orders = Order.objects.filter(id = self.kwargs['pk'])
        serializer = MealsToOrderSerializer(orders, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = MealsToOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChecksList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format = None):
        checks = Check.objects.all()
        serializer = CheckSerializer(checks, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = CheckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)