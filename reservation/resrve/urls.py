from django.urls import path
from . import views
from .views import BookingView, MenuView




urlpatterns = [
    path('', views.home_page),
    
    path('menu/', MenuView.as_view()),
    
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu-item')
]
