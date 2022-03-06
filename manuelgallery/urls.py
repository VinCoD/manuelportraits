from django.urls import path
from . import views

app_name = 'manuelgallery'

urlpatterns = [
    path('', views.index, name='index'),
]