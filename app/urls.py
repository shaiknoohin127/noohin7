from django.urls import path
from app.views import *
app_name='app'

urlpatterns=[
    path('one_view/',one_view,name='one_view'),
]