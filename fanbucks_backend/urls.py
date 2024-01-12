
from django.contrib import admin
from django.urls import path, include

from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('user/', views.UserView.as_view(), name='user'),
    path(r'api/auth/', include('knox.urls'))
]
