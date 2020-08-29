from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Table, ServicePercentage, Status
from .serializers import TableSerializer, ServicePercentageSerializer, StatusSerializer

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