from django.shortcuts import render

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=22074da11678f0c0fb4e4ba93841429e'
    return render(request,'weather/weather.html')