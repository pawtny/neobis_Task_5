from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Department, MealCategory, Meal
from .serializers import DepartmentSerializer, MealCategorySerializer, MealSerializer

class DepartmentList(APIView):
    def get(self, request, format = None):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentDetails(APIView):
    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def delete(self, request, pk, format=None):
        department = self.get_object(pk)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MealCategoryList(APIView):
    def get(self, request, format = None):
        mealcategories = MealCategory.objects.all()
        serializer = MealCategorySerializer(mealcategories, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = MealCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MealCategoryDetails(APIView):
    def get_object(self, pk):
        try:
            return MealCategory.objects.get(pk=pk)
        except MealCategory.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def delete(self, request, pk, format=None):
        mealcategory = self.get_object(pk)
        mealcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MealList(APIView):
    def get(self, request, format = None):
        meals = Meal.objects.all()
        serializer = DepartmentSerializer(meals, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MealDetails(APIView):
    def get_object(self, pk):
        try:
            return Meal.objects.get(pk=pk)
        except Meal.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        meal = self.get_object(pk)
        serializer = MealSerializer(meal)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        meal = self.get_object(pk)
        serializer = MealSerializer(meal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        meal = self.get_object(pk)
        meal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoriesByDepartmentView(APIView):
    def get(self, request, pk, format = None):
        categories = MealCategory.objects.filter(departmentid = self.kwargs['pk'])
        serializer = DepartmentSerializer(categories, many = True)
        return Response(serializer.data)