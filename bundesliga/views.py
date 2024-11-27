from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def GoalScorer(request):
    return HttpResponse('''<h2>Top Goal Scorer in Bundesliga of the Year 2022-23 season goes to</h2> <h1> FULLKRUG  !!</h1>
    <img src= 'https://tse1.mm.bing.net/th?id=OIP.QmKQqTIpVRs3A3OG0Rt-eAHaEi&pid=Api&P=0&h=180'>''')

def Midfielder(request):
    return HttpResponse('''<h2>Best Midfielder in Bundesliga of the year 2022-23 goes to</h2> <h1> FLORIAN WIRTZ !!</h1>
    <img src= 'https://assets.bundesliga.com/tachyon/sites/2/2021/02/florian-wirtz-leverkusen-b04.jpg?crop=38px,0px,1350px,1080px&fit=540,540'>''')
