from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('accounts/login/', views.custom_login,name='login'),
    path('create/',views.register,name='create'),
    path('token' , views.token_send , name="token_send"),
    path('success' , views.success , name='success'),
    path('verify/<auth_token>' , views.verify , name="verify"),
    path('error' ,views.error_page , name="error"),
    path('accounts/logout/', views.logout_view, name='logout'),
]