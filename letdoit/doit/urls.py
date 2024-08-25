from django.urls import path
from .views import *

urlpatterns = [
    path('', GoalCreateView.as_view(), name='goal-create'),
]
