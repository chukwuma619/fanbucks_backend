
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app import views

router = DefaultRouter()
router.register(r'bucks', views.BuckViewSet, basename='buck')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register/', views.RegisterView.as_view(), name='register'),
    path('api/auth/login/', views.LoginView.as_view(), name='login'),
    path('api/auth/logout/', views.LogoutView.as_view(), name="logout"),
    path('api/user/', views.UserView.as_view(), name='user'),
    path('api/', include(router.urls))
]
