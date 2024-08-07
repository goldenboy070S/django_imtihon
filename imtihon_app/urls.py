from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('c_photo/<int:c_id>', category_photo, name='photos'),
    path('details/<int:id>', detail, name='details')
]