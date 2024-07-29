from django.urls import path
from .views import factorial_view

urlpatterns = [
    path('', factorial_view, name='factorial_view'),
]
