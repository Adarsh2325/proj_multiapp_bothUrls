from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Top_GoalScorer(request):
    return HttpResponse('''<h2>Top Goal Scorer in Premier League of the Year 2022-23 season goes to</h2> <h1> ERLING HAALAND !!</h1> 
    <img src= 'https://www.sportsxm.com/wp-content/uploads/2022/09/Halaand.webp'>''')

def best_defender(request):
    return HttpResponse('''<h2>Best Defender Premier League of the year 2022-23 goes to</h2> <h1>Virgil van Dijk </h1>
    <img src= 'https://img.tripi.vn/cdn-cgi/image/width=700,height=700/https://gcs.tripi.vn/public-tripi/tripi-feed/img/481192MmS/anh-mo-ta.png'>''')
