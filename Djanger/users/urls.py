
from django.urls import path
from . import views

app_name = 'users'  # 关键设置：与namespace值一致

urlpatterns = [
    path('profile/', views.UtilTestViews.as_view(), name='profile'),
]