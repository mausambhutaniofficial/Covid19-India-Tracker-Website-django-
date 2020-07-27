from django.shortcuts import render
import requests
import json 
# Create your views here.
def home(request):
    url = "https://covid-193.p.rapidapi.com/statistics"
    querystring = {"country":"India"}
    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "2937c3a728mshad2d9d98c1fb590p181118jsn677ab7df0b24"
    }
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    data = response['response']
    #print(response)
    d = data[0]
    print(d)
    context = {
        'all':d['cases']['total'],
        'active':d['cases']['active'],
        'recovered':d['cases']['recovered'],
        'deaths':d['deaths']['total'],
        'new':d['cases']['new'],
        'critical':d['cases']['critical']
    }
    return render(request, 'index.html', context)