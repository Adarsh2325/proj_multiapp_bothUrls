from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Top_GK(request):
    return HttpResponse('''<h2>Top GK in SerieA League of the Year 2022-23 season goes to</h2> <h1> MICHELE DI GREGORIO !!</h1>
    <img src= 'https://tse1.mm.bing.net/th?id=OIP.xtwlFXdPLlu-yEkj36UMmQHaEi&pid=Api&P=0&h=180'>''' )

def best_midfielder(request):
    return HttpResponse('''<h2>Best Midfielder in SerieA League of the year 2022-23 goes to</h2> <h1>HAKAN CALHANOGLU !!</h1>
    <img src='https://tse1.mm.bing.net/th?id=OIP.Pvo5ZV9Im9iA_pYrVIOQzwHaE8&pid=Api&P=0&h=180'>''')