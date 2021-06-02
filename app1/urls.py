from django.urls import path

from app1.views import *

urlpatterns = [
    path('', Ejemplo),
    path('nuevo/', Ejemplo2, name = 'nuevo')

    ]