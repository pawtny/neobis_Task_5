from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from orders import views

urlpatterns = [
    path('tables/', views.TableList.as_view(), name = 'TableList'),
    path('tables/<int:pk>/', views.TableDetails.as_view(), name = 'TableDetails'),
    path('statuses/', views.StatusList.as_view(), name = 'StatusList'),
    path('statuses/<int:pk>/', views.StatusDetails.as_view(), name = 'StatusDetails'),
    path('servicepercentage/', views.ServicePercentageList.as_view(), name = 'ServicePercentageList'),
    path('servicepercentage/<int:pk>/', views.ServicePercentageDetails.as_view(), name = 'ServicePercentageDetails'),
    path('orders/', views.OrderList.as_view(), name = 'OrderList'),
    path('orders/<int:pk>', views.OrderDetails.as_view(), name = 'OrderDetails'),
    path('activeorders/', views.ActiveOrdersView.as_view(), name = 'ActiveOrders'),
    path('mealstoorder/', views.MealsToOrderView.as_view(), name = 'MealsToOrder'),
    path('mealstoorder/<int:pk>', views.MealsToOrderView.as_view(), name = 'MealsOfOrder'),
    path('checks/', views.ChecksList.as_view(), name = 'Checks'),
]

urlpatterns = format_suffix_patterns(urlpatterns)