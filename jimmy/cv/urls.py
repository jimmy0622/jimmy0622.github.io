from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_detail, name='cv_detail'),
]
