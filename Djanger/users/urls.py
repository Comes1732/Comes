
from django.urls import path
from .views import  RegisterView, LoginView

app_name = 'users'  # 关键设置：与namespace值一致

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'), # regis
    path('login/', LoginView.as_view(), name='login'),  # login
]
