from django.urls import path
from .views import apage

urlpatterns = [
    path('core', apage),
]