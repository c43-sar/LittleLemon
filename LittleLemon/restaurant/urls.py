from django.contrib import admin
from django.urls import path
# from .views import sayHello
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('', sayHello, name='sayHello'),
    path('', views.index, name='index'),
    path('menu/items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/items/<int:pk>/', views.SingleMenuItemView.as_view(),
         name='single-menu-item'),
    path('api-token-auth/', obtain_auth_token),
]
