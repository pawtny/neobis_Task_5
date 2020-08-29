from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import LoginAPIView, RegistrationAPIView, UserRetrieveUpdateDestroyAPIView, UserList, RoleList, RoleDetails

app_name = 'users'

urlpatterns = [
    path('user/', UserRetrieveUpdateDestroyAPIView.as_view()),
    path('users/', UserList.as_view(), name = 'userList'),
    path('users/reg', RegistrationAPIView.as_view(), name = 'userList'),
    path('users/login/', LoginAPIView.as_view()),
    path('roles/', RoleList.as_view()),
    path('roles/<int:pk>/', RoleDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
