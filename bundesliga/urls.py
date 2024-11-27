from django.urls import path

from bundesliga.views import *

urlpatterns=[
    path('GoalScorer/',GoalScorer,name='GoalScorer'),
    path('Midfielder/',Midfielder,name='Midfielder'),

]