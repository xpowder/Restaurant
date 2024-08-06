from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from resrve import views

# Set up the router for the BookingViewSet
router = DefaultRouter()
router.register(r'tables', views.BookingView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resrve.urls')),  
    path('api/', include('rest_framework.urls')),
    path('resrve/booking/', include(router.urls)),
]
