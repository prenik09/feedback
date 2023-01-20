from django.urls import path
from . import views

app_name='free'

urlpatterns=[
    path('',views.index,name='index'),
]