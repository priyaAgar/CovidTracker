import requests
from django.shortcuts import render
from urllib.request import urlopen # for fetching urls and provides a simple interface
import json # to parse the string (output into json object)
# install requests==2.24.0
# install urllib3==1.25.10

def home(request):
    data = []
    url = "https://covid-193.p.rapidapi.com/statistics"   # key from rapidApi Site

    querystring = {"country": "India"}     #change country name acc. to you

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "be7f37114bmsh38c0486c35a5050p1bc1e5jsnf574155ad041"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json() # a dictionary returned with information
    d = response['response'] # list with information of your country
    s = d[0] # only one item thus index 0
    context = {
        'all': s['cases']['total'],
        'recovered': s['cases']['recovered'],
        'deaths': s['deaths']['total'],
        'new': s['cases']['new'],
        'serious': s['cases']['critical'],
    }
    return render(request, 'index.html', context)