from django.contrib import admin
from django.urls import include, path
from meals import views

urlpatterns = [
    path('', include('users.urls')),
    path('', include('meals.urls')),
    path('', include('orders.urls')),
    path('admin/', admin.site.urls),
]
