
from django.urls import path
from . import views

app_name = 'utils'  # 关键设置：与namespace值一致

urlpatterns = [
    path('test_url/', views.UtilTestViews.as_view(), name='test_url'),
]