from django.urls import path

from .views import *

urlpatterns = [
    path('', menu, name='menu'),
    path('rubric/<int:pk>', get_rubric, name = 'rubric'),

]
