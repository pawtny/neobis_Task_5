from django.contrib import admin
from django.urls import include, path
from meals import views
from django.conf.urls import include

urlpatterns = [
    path('', include('users.urls')),
    path('', include('meals.urls')),
    path('', include('orders.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
