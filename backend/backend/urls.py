from django.urls import path, include
from textile.views import home, textile_data

urlpatterns = [
    path('', home, name='home'),  # This line will match the root URL
    path('api/textile/', textile_data, name='textile_data'),
]