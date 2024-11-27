from django.urls import path

from laliga.views import *

urlpatterns=[
    path('GoalScorer/',GoalScorer,name='GoalScorer'),
    path('Midfielder/',Midfielder,name='Midfielder'),


]