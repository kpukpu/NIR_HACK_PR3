from django.urls import path
from .views import delete
from . import views

urlpatterns = [ 
    path('geo_code/', views.geocode, name = 'geocode'), # 대출 가능 도서 목록
]