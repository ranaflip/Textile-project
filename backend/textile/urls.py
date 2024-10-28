from django.urls import path
from . import views

urlpatterns = [
    path('api/textile/', views.textile_data, name='textile_data')
]
