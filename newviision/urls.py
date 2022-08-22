from django.urls import path

from . import views

urlpatterns = [
     path('',views.home, name='homeon'),
     path('addin',views.add, name='addin'),
     path('adddzz',views.addd, name='adddzz')
]