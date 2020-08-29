from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from meals import views

urlpatterns = [
    path('departments/', views.DepartmentList.as_view(), name = 'DepartmentList'),
    path('departments/<int:pk>/', views.DepartmentDetails.as_view(), name = 'DepartmentDetails'),
    path('mealcategories/', views.MealCategoryList.as_view(), name = 'MealCategoryList'),
    path('mealcategories/<int:pk>/', views.MealCategoryDetails.as_view(), name = 'MealCategoryDetails'),
    path('meals/', views.MealList.as_view(), name = 'MealList'),
    path('meals/<int:pk>', views.MealDetails.as_view(), name = 'MealDetails'),
    path('categoriesbydepartment/<int:pk>', views.CategoriesByDepartmentView.as_view(), name = 'CategoriesByDepartment'),
]

urlpatterns = format_suffix_patterns(urlpatterns)