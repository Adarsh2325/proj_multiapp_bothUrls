from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def GoalScorer(request):
    return HttpResponse('''<h2>Top Goal Scorer in Laliga League of the Year 2022-23 season goes to</h2> <h1> ROBERT LEWANDOWSKI  !!</h1>
    <img src= 'https://tse2.mm.bing.net/th?id=OIP.r8lDOLxiOX-F3wZLXeTpXgHaEE&pid=Api&P=0&h=180'>''')

def Midfielder(request):
    return HttpResponse('''<h2>Best Midfielder in Laliga League of the year 2022-23 goes to</h2> <h1> TONY KROOS !!</h1>
    <img src= 'https://cdn.vox-cdn.com/thumbor/qtzkOnzbhKPNo_yYqbt7DG294Zk=/0x0:4012x2429/1200x800/filters:focal(1871x489:2511x1129)/cdn.vox-cdn.com/uploads/chorus_image/image/72975982/1864810076.0.jpg'>''')