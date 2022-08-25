from django.urls import path
from .views import *

urlpatterns = [
    path('', UserList.as_view()),
    path('add', UserCreateView.as_view()),
    path('<int:pk>/', UserUpdateView.as_view()),
    path('del/<int:pk>/', UserDeleteView.as_view()),
]